from typing import List
from matplotlib import pyplot as plt

import numpy as np
from .facets import normal_at_point, angle_between, get_coincident_points


class ParallelFaceFinder():

    ANG_TOL_DEG = np.radians(5)  # 1 degree
    SHOW_PLOTS = False

    def __init__(self, points, connections) -> None:
        self.points = points
        self.connections = connections
        self.parallel_faces = []
        self.non_parallel_faces = []

    def find(self, face: List) -> List[List[int]]:
        """Returns all faces that are parallel to the `face` at any of their common points

        Parameters
        ----------
        face : List
            List of points that define a face

        Returns
        -------
        List[List]
            List of faces that are parallel to `face`
        """
        if face not in self.parallel_faces:
            self.parallel_faces.append(face)

        for candidate_face in (f for f in self.connections if f not in (self.parallel_faces
                                                                        + self.non_parallel_faces)):

            # All the points that are coincident to any point in the candidate face
            coincident_points = [pt for cpt in candidate_face
                                 for pt in get_coincident_points(cpt, self.points)]

            # For every point on the face that is coincident to a point on the candidate face
            # found = False
            for point in (p for p in face if p in coincident_points):

                # Get the normals at the common point
                local_candidate_normal = normal_at_point(candidate_face, point, self.points)
                local_face_normal = normal_at_point(face, point, self.points)
                angle = angle_between(local_candidate_normal, local_face_normal)

                # Check if the normals are parallel
                if angle < self.ANG_TOL_DEG:

                    if self.SHOW_PLOTS:
                        ax = self.plot(c='k')
                        ax.plot(*np.array(self.points)[face].T, c='b')
                        ax.plot(*np.array(self.points)[candidate_face].T, c='r', ls='--')
                        ax.scatter(*np.array(self.points)[point].T, s=100, c='gray')
                        ax.plot(*np.array([np.array(self.points)[point],
                                np.array(self.points)[point]+local_face_normal]).T, c='b')
                        ax.plot(*np.array([np.array(self.points)[point], np.array(self.points)
                                [point]+local_candidate_normal]).T, c='r', ls='--')
                        ax.set_title(f'Angle: {np.degrees(angle):0.2f}')
                        ax.axis('equal')

                    self.parallel_faces.append(candidate_face)
                    self.find(candidate_face)
                    # found = True
                    break

            # if not found:
            #     self.non_parallel_faces.append(candidate_face)

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
