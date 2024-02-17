"""Module containing :class:`WearableShell`"""
import json
from functools import lru_cache
from pathlib import Path
from typing import List

import numpy as np
import pandas as pd
from aviewpy.contact import get_contact_data
from aviewpy.files import shell
from aviewpy.objects import unique_object_name
from aviewpy.variables import set_dv
from matplotlib import pyplot as plt
from numpy.typing import ArrayLike
from scipy.spatial import cKDTree


from .archard import wear_rate
from .facets import angle_between, get_coincident_points, normal_at_point
from .parallel_face_finder import ParallelFaceFinder
from .utils.plane import plane_normal_from_points
from .utils.utils import three_point_area, unique_path

from Analysis import Analysis  # type: ignore # noqa # isort:skip
from Geometry import GeometryShell  # type: ignore # noqa # isort:skip

_XYZ = ['x', 'y', 'z']
PARALLEL_NORMAL_TOL = np.radians(5)  # 1 degree
WEAR_SUFFIX = '.wear'


class WearableShell():
    """A subclass of the Adams shell geometry class :class:`GeometryShell` for 
    which the wear that accumulates during a given analysis can be 
    calculated and applied (geometry modified) for a subsequent analysis.

    Note
    ----
    Some formulations of the Archard equation use a *dimensionless* wear coefficient (K)
    and a hardness coefficient (H). This implementation uses a *dimensional* wear 
    coefficient (K_d) given as:

        K_d = K/H

    References
    ----------
    * J. F. Archard, “Contact and Rubbing of Flat Surfaces,” Journal of Applied Physics, vol. 
    24, no. 8, pp. 981–988, Aug. 1953, doi: 10.1063/1.1721448.
    """

    def __init__(self, geom: GeometryShell):
        """Initialize a `WearableShell`. 

        Parameters
        ----------
        geom : GeometryShell
            An existing Adams shell geometry
        k_d : float
            The **dimensional** wear coefficient.
        """
        # db_key = find_by_full_name(geom.full_name)
        # super().__init__(db_key)

        self.wear_data: pd.DataFrame = None
        self.kd_tree: cKDTree = None
        self._obj = geom

        self.name = str(geom.name)
        self.full_name = str(geom.full_name)
        self.parent = geom.parent
        self.points, self.facets = shell.drop_duplicates(*shell.read_shell_file(geom.file_name))
        self.connections_ = None

        self.reference_marker = geom.reference_marker
        self.file_name = geom.file_name

        self._nominal_element_size = None

    @property
    def connections(self):
        if self.connections_ is None:
            self.connections_ = [[np.argmin(np.linalg.norm(np.array(self.points) -
                                                           np.array(self._obj.points[ip]),
                                                           axis=1))
                                  for ip in f]
                                 for f in self._obj.connections]

        return self.connections_

    def get_volume(self):
        """Get the volume of the shell"""
        return shell.get_shell_volume(np.array(self.points), np.array(self.facets))

    def write_wear_data(self, path: Path):
        """Write the wear data to a pickle file

        Parameters
        ----------
        path : Path
            The path to write the file to
        """
        if self.wear_data is not None:
            self.wear_data.to_pickle(path.with_suffix('.pkl'))
        else:
            raise ValueError('No wear data to write!')

    def read_wear_data(self, path: Path):
        """Read the wear data to a pickle file

        Parameters
        ----------
        path : Path
            The path to read the file from
        """
        self.wear_data = pd.read_pickle(path.with_suffix('.pkl'))
        path.with_suffix('.pkl').unlink()

    def calculate_wear(self, ans: Analysis, k_d: float, res_comp_name: str = None):
        """Calculates the wear that accumulated in the given `Analysis`

        Parameters
        ----------
        ans : Analysis
            Adams Analysis object for which to calculate wear
        """
        data = self.get_contact_data(ans)

        # Round the coordinates
        data[['loc_x', 'loc_y', 'z']] = (data[['loc_x', 'loc_y', 'loc_z']]
                                         .round(-self.element_size_order + 1))

        # Rename Unit Vectors
        data = data.rename(columns={f'normal_unit_{d}': f'u_{d}' for d in _XYZ})

        # Calculate the wear rate
        data['dQ'] = wear_rate(data['normal'], data['slip'], k_d)

        # Calculate the total wear volume (at each coordinate) (not cumulative)
        data['Q'] = data['dQ'] * data['step']

        # Calculate the instantaneous wear volume vectors
        data[['Q_x', 'Q_y', 'Q_z']] = (data[[f'u_{d}' for d in _XYZ]].multiply(data['Q'], axis=0))

        # Calculate the cylindrical coordinates
        data['loc_r'] = data[['loc_x', 'loc_y']].apply(np.linalg.norm, axis=1)
        data['loc_phi'] = np.arctan2(data['loc_y'], data['loc_x'])

        # Check wear log to see if this analysis has already been applied to this leadscrew
        ans_props = {p: getattr(ans, p) for p in ans.properties if p not in ('results', 'parent')}
        if '_wear_log' in self._obj.DesignVariables:
            wear_log = self._obj.DesignVariables['_wear_log'].value
        else:
            wear_log = []

        if exists_in_log(ans_props, wear_log):
            raise AnalysisRepeatError('Wear from this analysis has already been applied!')

        # Write wear data
        wear_file = Path(self._obj.file_name).with_suffix(WEAR_SUFFIX)
        data.to_pickle(wear_file)

        # Add to the wear data log
        wear_log.append(json.dumps({**ans_props,
                                    'shell_file': self._obj.file_name,
                                    'wear_file': str(wear_file)}))

        # Set the wear log design variable
        set_dv(self._obj, '_wear_log', wear_log)

        self.wear_data = data

    def apply_wear(self, scale_factor=1.0, patch_size_factor=1.0, copy_original=True):
        """Apply wear calculated by :meth:`calculate_wear`

        Parameters
        ----------
        scale_factor : float, optional
            A scale factor on the distance to adust the points, by default 1.0
        patch_size_factor : float, optional
            A factor for controlling the size of the contact patch. A value of 1 means
            the contact patch is roughly the size of one facet, by default 1.0

        Returns
        -------
        pd.DataFrame
            DataFrame of wear vectors
        """
        if len(self.wear_data) != 0:

            # Get the points that are in contact
            self.wear_data['points'] = self.get_wear_points(self.wear_data, patch_size_factor)

            if (self.wear_data['points'].apply(len) == 0).any():
                if False:
                    # Drop rows with no points
                    self.wear_data = self.wear_data[self.wear_data['points'].apply(len) != 0]
                else:
                    raise ValueError('Some contact incidents were not assigned to points in the shell!')

            # Calculate the wear vectors
            def _get_vec(row: pd.Series, use_facet_normal=False):
                idx_points = row['points']
                contact_normal = (row[[f'Q_{d}' for d in _XYZ]]
                                  / np.linalg.norm(row[[f'Q_{d}' for d in _XYZ]]))

                # Get the normal
                if use_facet_normal:

                    # Get the all the facets which contain any of `idx_points` **and** are in the face
                    # who's normal is closest to the contact normal
                    face = self.face_perp_at_point(idx_points[0], contact_normal)
                    facets = [facet for facet in self.facets
                              if any(ipt in facet for ipt in idx_points)
                              and all(ipt in face for ipt in facet)]

                    facet_normals = []
                    for facet in facets:
                        facet_normal = plane_normal_from_points(*np.array(self.points)[np.array(facet)])

                        # Reverse the face normal if necessary
                        if np.sign(facet_normal[0]) != np.sign(contact_normal[0]):
                            facet_normal = -1 * facet_normal

                        facet_normals.append(facet_normal)

                    # Take the mean facet normal
                    sum_norm = np.array(facet_normals).sum(axis=0)
                    normal = sum_norm / np.linalg.norm(sum_norm)

                else:
                    normal = contact_normal

                dist = row['Q'] * scale_factor / self.nodal_area(idx_points, in_plane=normal)

                return pd.Series(dist * normal)

            df_vec = self.wear_data[['points']]
            df_vec[['d_x', 'd_y', 'd_z']] = self.wear_data.apply(_get_vec, axis=1)

            df_vec = (df_vec
                      .explode('points')
                      .groupby('points')
                      .sum()
                      .rename_axis('point'))

            # Modify the shell's points to account for the wear
            for point, vec in df_vec.iterrows():
                self.points[point] = tuple(np.array(self.points)[point] + vec.to_numpy())

        new_shell_file = unique_path(Path(self.file_name).name)
        shell.write_shell_file(points=self.points,
                               facets=self.facets,
                               file_name=new_shell_file,
                               scale=.0254)

        if copy_original:
            desired_full_name = f'{self._obj.parent.full_name}.{self._obj.name}_unworn_0'
            new_name = unique_object_name(desired_full_name).split('.')[-1]
            orig: GeometryShell = self._obj.copy(new_name=new_name)
            orig.active = 'off'
            orig.visibility = 'off'

        self._obj.file_name = str(new_shell_file)
        self.file_name = str(new_shell_file)

    def get_wear_points(self, wear_data: pd.DataFrame, patch_size_factor=None):
        """Finds the points that are closest to the coordinates provided

        Parameters
        ----------
        df_loc : pd.DataFrame
            Coordinate DatFrame with columns 'x', 'y', 'z'
        patch_size_factor : float
            A factor determining how large the contact patch is. The contact patch is equal to the 
            nominal element size times this factor. If None, all points on the contact face.

        Returns
        -------
        List[List[int]]
            A list of length N of the points found for each coordinate 
        """
        if self.kd_tree is None:
            self.kd_tree = cKDTree(np.array(self.points))  # pylint: disable=not-callable

        xyz = wear_data[[f'loc_{d}' for d in _XYZ]].to_numpy()
        if patch_size_factor is not None:
            search_radius = self.nominal_element_size * patch_size_factor

            points: List[List[int]] = self.kd_tree.query_ball_point(xyz,
                                                                    r=search_radius,
                                                                    n_jobs=-1)
        else:

            # Use all points, they will be filtered later
            points: List[List[int]] = [list(range(len(self.points))) for _ in range(len(xyz))]

        normals = ((wear_data[[f'Q_{d}' for d in _XYZ]]
                    / np.linalg.norm(wear_data[[f'Q_{d}' for d in _XYZ]]))
                   .rename(columns={f'Q_{d}': d for d in _XYZ}))

        filtered_points = []
        for idx, normal in normals.reset_index(drop=True).iterrows():
            # Sort the points by ascending distance from conact location
            sort_pts = sorted(points[idx],
                              key=lambda i: np.linalg.norm(np.array(self.points[i]) - xyz[idx]))      # pylint: disable=cell-var-from-loop

            # Filter the points
            filt_pts = self.filter_points(sort_pts, normal)

            # Append
            filtered_points.append(filt_pts)

        return filtered_points

    def filter_points(self, points: List[int], normal: ArrayLike):
        """Finds the face from `self.connections` that 
        * contains `points[0]`
        * has the closest normal to `normal_unit`
        Returns only points that are on that face OR points that are coincident to points on 
        that face

        Parameters
        ----------
        points : List[int]
            List of points sorted by ascending distance
        normal_unit : ArrayLike
            Contact unit vector

        Returns
        -------
        ArrayLike
            Filtered points lists
        """
        # For each face get the angle between the contact and the face normal at the closest point
        perp_face = self.face_perp_at_point(points[0], normal)

        # Need to add all the faces that are parallel to the perp_face
        parallel_faces = self.get_parallel_faces(perp_face)

        # Return only the points that are on the parallel faces
        points_to_return = [i_pt for i_pt in points if any(i_pt in f for f in parallel_faces)]

        # Add any points that are coincident to points on the parallel faces
        points_to_return = [i_pt for i_pt in points
                            if any(self.points[i_pt] == self.points[j_pt]
                                   for j_pt in points_to_return)]

        return points_to_return

    @lru_cache
    def _get_parallel_faces(self, idx_face) -> List[List[int]]:
        """A cached version of `get_parallel_faces`

        Parameters
        ----------
        idx_face : int
            Index of the face to find parallel faces to

        Returns
        -------
        List[List[int]]
            List of faces that are parallel to the face at `idx_face`
        """
        face = self.connections[idx_face]
        finder = ParallelFaceFinder(self.points, self.connections)
        finder.find(face)
        return finder.parallel_faces

    def get_parallel_faces(self, face: List) -> List[List[int]]:
        """Returns all faces that are parallel to `face`

        Parameters
        ----------
        face : List
            List of points that define a face

        Returns
        -------
        List[List]
            List of faces that are parallel to `face`
        """
        return self._get_parallel_faces(self.connections.index(list(face)))

    def face_perp_at_point(self, idx_point: int, vec: pd.Series) -> List[int]:

        # get all points coincident to idx_point
        idx_coinc_points = get_coincident_points(idx_point, self.points)

        # List the potential faces (any face that contains point)
        faces = [np.array(f) for f in self.connections if any(i in f for i in idx_coinc_points)]
        angle_between_normals = []
        for face in faces:
            face_normal = self.normal_at_point(face, idx_point)

            # Reverse the face normal if necessary
            if np.sign(face_normal[0]) != np.sign(vec[0]):
                face_normal = -1 * face_normal

            angle_between_normals.append(angle_between(face_normal, vec))

        # Take the "most perpendicular" face
        perp_face = faces[np.argmin(angle_between_normals, axis=0)]

        if False:
            ax = self.plot(c='k')
            pt = np.array(self.points[idx_point])
            ln = np.array([pt, pt + vec.to_numpy()])
            ax.plot(*ln.T)

            ax.plot(np.array(self.points)[perp_face, 0], np.array(self.points)[perp_face, 1], np.array(self.points)[perp_face, 2])

        return perp_face

    def normal_at_point(self, face: ArrayLike, idx_point: int):
        """Gets the normal of a face at a particular point

        Notes
        -----
        * `face` must be an argument because a point could be on multiple faces
        * Assumes a smooth face
        * `idx_point` need not be on the face, but must be coincident to a point on the face

        Parameters
        ----------
        face : ArrayLike
            An array of indices of points which make up a face on the shell
        idx_point : int
            The index of the point at which the normal should be taken

        Returns
        -------
        NDArray
            A unit vector representing the face normal at that point
        """
        return normal_at_point(face, idx_point, self.points)

    def get_contact_data(self, ans: Analysis) -> pd.DataFrame:
        """Gets a DataFrame of contact data needed for calculating wear.

        Parameters
        ----------
        ans : Analysis
            The Adams analysis for which wear will be calculated

        Returns
        -------
        pd.DataFrame
            A DataFrame of contact data needed for calculating wear
        """
        return get_contact_data(self._obj, ans, self.reference_marker)

    def nodal_area(self, idx_points: List[int], in_plane: List[float] = None):
        """Calculates the area of a list of quasi-planar points

        Parameters
        ----------
        idx_points : List[int]
            Indices of points that are adjacent and planar
        in_plane : List[float], optional
            A plane that the points should be projected to before calculating the area, 
            by default None

        Returns
        -------
        float
            The area of the shape that encompasses the points
        """
        # Get the areas of all the facets whose points are **all** in `idx_points`
        df = pd.DataFrame(self.facets)
        df['n_in_patch'] = df.isin(idx_points).sum(axis=1)

        areas = []
        for _, row in df[df['n_in_patch'] > 0].iterrows():
            facet = row[[0, 1, 2]].values
            pts = np.array(self.points)[facet]
            area = three_point_area(pts[0], pts[1], pts[2], in_plane=in_plane)
            area = area * row['n_in_patch'] / 3
            areas.append(area)

        return sum(areas)

    @property
    def nominal_element_size(self):
        """Returns the median element size.
        """
        if self._nominal_element_size is None:
            dists_mag = []
            for facet in self.facets:
                dists_xyz = np.diff(np.array(self.points)[np.array(facet)], axis=0)
                dists_mag.extend(np.apply_along_axis(np.linalg.norm, 1, dists_xyz))

            self._nominal_element_size = np.median(dists_mag)

        return self._nominal_element_size

    def facets_by_connection(self, connection):
        """The facets in the given connection

        Parameters
        ----------
        connection : List[int]
            A list of connected point indices (i.e, a single row from `self.connections`)

        Returns
        -------
        List[List[int]]
            A list of triplets representing the shell facets
        """
        return np.array([list(el) for el in zip(connection[::2],
                                                connection[1::2],
                                                connection[2::2])])

    def plot(self, ax=None, **kwargs):
        """Plots the geometry

        Parameters
        ----------
        ax : matplotlib.axes.Axes, optional
            The axes to plot on, by default None
        """
        if ax is None:
            fig = plt.figure()
            ax = fig.add_subplot(projection='3d')

        pts = np.array(self.points)
        ax.scatter(pts[:, 0], pts[:, 1], pts[:, 2], **kwargs)

        for idx, face in enumerate(self.connections):
            ax.plot(pts[face, 0], pts[face, 1], pts[face, 2], label=str(idx), **kwargs)

        ax.axis('equal')
        return ax

    @property
    def facets_from_file(self):
        """Facets (elements) of the geometry

        Returns
        -------
        List[List[int]]
            A list of triplets representing the shell facets
        """
        _, facets = shell.read_shell_file(self.file_name)
        return np.array(facets)

    @property
    def element_size_order(self):
        """Returns the log of `self.nominal_element_size`
        """
        return round(np.log10(self.nominal_element_size))


def exists_in_log(ans_props: dict, log: List[dict]):
    """Checks :arg:`log` for existence of :arg:`ans_props`

    Parameters
    ----------
    ans_props : dict
        A dictionary of properties describing an Adams :class:`Analysis`
    log : List[dict]
        A list of of properties describing Adams :class:`Analysis` objects that have been 
        previously logged

    Returns
    -------
    bool
        True if :arg:`ans_props` already exists in :arg:`log`
    """
    for line in log:
        log_props = json.loads(line)

        if all(ans_props[k] == log_props[k] for k in log_props):
            return True

    return False


class AnalysisRepeatError(Exception):
    """Raised if wear is applied for the same analysis twice
    """
