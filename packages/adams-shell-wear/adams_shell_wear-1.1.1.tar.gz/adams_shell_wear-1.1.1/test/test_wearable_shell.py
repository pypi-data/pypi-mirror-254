# pylint: disable=missing-function-docstring, missing-class-docstring, missing-module-docstring
import sys
import unittest
from pathlib import Path

import numpy as np
import pandas as pd
import pygmsh
from aviewpy.files.bin import write_bin_file
from aviewpy.files.shell import write_shell_file
from aviewpy.variables import set_dv
from Geometry import GeometryShell  # type: ignore # noqa

from adams_shell_wear.wearable_shell import WearableShell

import Adams  # type: ignore # noqa #isort: skip
from Part import Part  # type: ignore # noqa #isort: skip
from Marker import Marker  # type: ignore # noqa #isort: skip


K_D = 1e-8
RESOURCES = Path(__file__).parent / 'resources'


class Test_Init(unittest.TestCase):
    """Tests related to creating a :class:`WearableShell` instance
    """

    def setUp(self):
        self.mod = Adams.Models.create()
        self.part = self.mod.Parts.createRigidBody()
        self.mkr = self.part.Markers.create()
        self.geom: GeometryShell = self.part.Geometries.createShell(
            file_name=str(RESOURCES/'latch_tooth.shl'),
            reference_marker=self.mkr
        )

    def test_can_initialize_without_error(self):
        shell = WearableShell(self.geom)

    def tearDown(self):
        for mod in Adams.Models.values():
            mod.destroy()

class Test_Wear(unittest.TestCase):

    EXPECTED_CONTACT_DATA_FILE = Path(__file__).parent / 'expected/contact_data.pkl'
    EXPECTED_WEAR_DATA_FILE = Path(__file__).parent / 'expected/wear_data.pkl'
    EXPECTED_WORN_POINTS_FILE = 'test/expected/worn_points.pkl'
    EXPECTED_WORN_FACETS_FILE = 'test/expected/worn_facets.pkl'

    VAULT = Path(__file__).parent / 'vault'
    TMP_FILES = Path(__file__).parent / 'tmp'

    def setUp(self):
        for mod in Adams.Models.values():
            mod.destroy()

        bin_file = RESOURCES / 'sphere_on_tooth.bin'
        Adams.execute_cmd(f'file bin read file="{bin_file}" alert=no')
        self.mod = Adams.getCurrentModel()
        geom = self.mod.Parts['tooth'].Geometries['SHELL_1']
        self.shell = WearableShell(geom)
        self.ans = next(a for a in self.mod.Analyses.values())

    def test_get_contact_data_returns_expected_normal_values(self):
        expected = pd.read_pickle(self.EXPECTED_CONTACT_DATA_FILE)
        actual = self.shell.get_contact_data(self.ans)

        self.assertTrue(np.allclose(expected['normal'], actual['normal']))

    def test_calculate_wear(self):
        expected = pd.read_pickle(self.EXPECTED_WEAR_DATA_FILE)
        self.shell.calculate_wear(self.ans, K_D)

        self.assertTrue(np.allclose(expected['Q'], self.shell.wear_data['Q']))

    def test_apply_wear(self):
        self.shell.calculate_wear(self.ans, K_D)
        self.shell.apply_wear(scale_factor=1e3, patch_size_factor=2)
        write_bin_file(str(self.VAULT / 'worn.bin'))
        with Path(self.shell._obj.file_name).open('r') as fid:                                      # pylint: disable=protected-access
            n_points, n_facets, scale = map(float, fid.readline().split())

        points_actual = pd.read_csv(self.shell._obj.file_name,                                      # pylint: disable=protected-access
                                    names=['x', 'y', 'z'],
                                    skiprows=1,
                                    delimiter=' ',
                                    nrows=n_points).to_numpy()

        facets_actual = pd.read_csv(self.shell._obj.file_name,                                      # pylint: disable=protected-access
                                    header=None,
                                    skiprows=int(1+n_points),
                                    delimiter=' ',
                                    nrows=n_facets).drop(0, axis=1).to_numpy()

        points_expected = np.load(self.EXPECTED_WORN_POINTS_FILE, allow_pickle=True)
        facets_expected = np.load(self.EXPECTED_WORN_FACETS_FILE, allow_pickle=True)

        self.assertTrue(np.allclose(points_actual, points_expected))
        self.assertTrue(np.allclose(facets_actual, facets_expected))

    def test_write_and_read_wear_data(self):
        self.shell.calculate_wear(self.ans, K_D)
        self.shell.apply_wear(scale_factor=1e3, patch_size_factor=2)
        self.shell.write_wear_data(self.TMP_FILES / 'wear_data.pkl')

        geom = self.mod.Parts['tooth'].Geometries['SHELL_1']
        shell_from_read = WearableShell(geom)
        shell_from_read.read_wear_data(self.TMP_FILES / 'wear_data.pkl')
        self.assertTrue(np.allclose(self.shell.wear_data['Q'], shell_from_read.wear_data['Q']))
    
    def test_volume_change_is_correct_single_wear_point(self):
        unworn_vol = self.shell.get_volume()
        # scale_factor = 5e4
        # data = pd.read_csv(RESOURCES / 'single_wear.csv')
        # data[['Q', 'Q_x', 'Q_y', 'Q_z']] = data[['Q', 'Q_x', 'Q_y', 'Q_z']]*scale_factor
        data = pd.DataFrame({'loc_x': [0],
                                  'loc_y': [0],
                                  'loc_z': [0],
                                  'Q': [1e-3],
                                  'Q_x': [1e-3],
                                  'Q_y': [0],
                                  'Q_z': [0]})
        self.shell.wear_data = data
        self.shell.apply_wear(patch_size_factor=None)
        worn_vol = self.shell.get_volume()
        calculated_total_wear = self.shell.wear_data['Q'].sum()
        actual_volume_change = unworn_vol-worn_vol
        self.assertAlmostEqual(calculated_total_wear, actual_volume_change)

    def test_volume_change_is_correct(self):
        unworn_vol = self.shell.get_volume()
        self.shell.calculate_wear(self.ans, K_D*1e3)
        self.shell.apply_wear(patch_size_factor=2)
        worn_vol = self.shell.get_volume()
        calculated_total_wear = self.shell.wear_data['Q'].sum()
        actual_volume_change = unworn_vol-worn_vol
        self.assertAlmostEqual(calculated_total_wear, actual_volume_change)

    def tearDown(self):
        for mod in Adams.Models.values():
            mod.destroy()

class Test_RectangleWear(unittest.TestCase):

    def setUp(self):
        for mod in Adams.Models.values():
            mod.destroy()
        
        mod = Adams.Models.create()
        box_part: Part = mod.Parts.createRigidBody(name='box', density=.28)
        
        box_geom = make_cube_shell(box_part.Markers.create(name='ref_mkr', location=[-.5, -.5, -.5]), name='box_geom')
        # make_the_rest_of_the_model(mod, box_geom)
        
        self.shell = WearableShell(box_geom)

    def test_worn_volume_is_correct_for_entire_box_face_centered(self):
        """Wear is applied at the center of the -x face of the box. `patch_size_factor` is None
        so the entire face of the box should be worn. The volume of the box should be reduced by the
        volume of the wear"""
        # Get unworn volume
        unworn_vol = self.shell.get_volume()

        # Apply Wear
        wear_data = pd.DataFrame({'loc_x': [0],
                                  'loc_y': [0.5],
                                  'loc_z': [0.5],
                                  'Q': [1e-2],
                                  'Q_x': [1e-2],
                                  'Q_y': [0],
                                  'Q_z': [0]})
        self.shell.wear_data = wear_data
        self.shell.apply_wear(patch_size_factor=None)

        # Get worn volume
        worn_vol = self.shell.get_volume()
        
        # Get Calculated Volume Change
        calculated_total_wear = self.shell.wear_data['Q'].sum()

        # Get Actual Volume Change
        actual_volume_change = unworn_vol-worn_vol

        # Compare
        self.assertAlmostEqual(calculated_total_wear, actual_volume_change)

    def test_worn_volume_is_correct_for_entire_box_face_corner(self):
        """Same as previous test, but applied at the corner of the box. The same thing should happen
        since the fitering algorithm should find the -x face has the closest normal to the wear
        normal."""
        # Get unworn volume
        unworn_vol = self.shell.get_volume()

        # Apply Wear
        wear_data = pd.DataFrame({'loc_x': [0],
                                  'loc_y': [0],
                                  'loc_z': [0],
                                  'Q': [1e-2],
                                  'Q_x': [1e-2],
                                  'Q_y': [0],
                                  'Q_z': [0]})
        self.shell.wear_data = wear_data
        self.shell.apply_wear(patch_size_factor=None)

        # Get worn volume
        worn_vol = self.shell.get_volume()
        
        # Get Calculated Volume Change
        calculated_total_wear = self.shell.wear_data['Q'].sum()

        # Get Actual Volume Change
        actual_volume_change = unworn_vol-worn_vol

        # Compare
        self.assertAlmostEqual(calculated_total_wear, actual_volume_change)

    def test_worn_volume_is_correct_for_partial_box_face_centered(self):
        """Wear is applied at the center of the -x face of the box. `patch_size_factor` is 1
        so only part of the face of the box should be worn. The volume of the box should be reduced 
        by the volume of the wear."""
        # Get unworn volume
        unworn_vol = self.shell.get_volume()

        # Apply Wear
        wear_data = pd.DataFrame({'loc_x': [0],
                                  'loc_y': [0.5],
                                  'loc_z': [0.5],
                                  'Q': [1e-2],
                                  'Q_x': [1e-2],
                                  'Q_y': [0],
                                  'Q_z': [0]})
        self.shell.wear_data = wear_data
        self.shell.apply_wear(patch_size_factor=1)

        # Get worn volume
        worn_vol = self.shell.get_volume()
        
        # Get Calculated Volume Change
        calculated_total_wear = self.shell.wear_data['Q'].sum()

        # Get Actual Volume Change
        actual_volume_change = unworn_vol-worn_vol

        # Compare
        self.assertAlmostEqual(calculated_total_wear, actual_volume_change)

    def test_worn_volume_is_correct_for_partial_box_face_offset(self):
        """Wear is applied at the center of the -x face of the box. `patch_size_factor` is 1
        so only part of the face of the box should be worn. The volume of the box should be reduced 
        by the volume of the wear."""
        # Get unworn volume
        unworn_vol = self.shell.get_volume()

        # Apply Wear
        wear_data = pd.DataFrame({'loc_x': [0, 0],
                                  'loc_y': [0.56315, 0.43685],
                                  'loc_z': [0.58268, 0.41732],
                                  'Q': [1e-2, 1e-2],
                                  'Q_x': [1e-2, 1e-2],
                                  'Q_y': [0, 0],
                                  'Q_z': [0, 0]})
        self.shell.wear_data = wear_data
        self.shell.apply_wear(patch_size_factor=1)

        # Get worn volume
        worn_vol = self.shell.get_volume()
        
        # Get Calculated Volume Change
        calculated_total_wear = self.shell.wear_data['Q'].sum()

        # Get Actual Volume Change
        actual_volume_change = unworn_vol-worn_vol

        # Compare
        self.assertAlmostEqual(calculated_total_wear, actual_volume_change)

    def tearDown(self):
        return

class Test_LongRectangleWear(unittest.TestCase):

    def setUp(self):
        for mod in Adams.Models.values():
            mod.destroy()
        
        mod = Adams.Models.create()
        box_part: Part = mod.Parts.createRigidBody(name='box', density=.28)

        box_geom = make_long_rect_shell(box_part.Markers.create(name='ref_mkr',
                                                                location=[-.5, -.5, -.5]),
                                        edge_length=2,
                                        name='box_geom')
        
        self.shell = WearableShell(box_geom)

    def test_long_rectangle_wear(self):
        # Get unworn volume
        unworn_vol = self.shell.get_volume()

        # Apply Wear
        n_points = 200
        y = np.linspace(0.5, 3.5, n_points)
        helix_angle = np.radians(15)
        Q_x = 1e-2*np.ones(n_points)*np.cos(helix_angle)
        Q_y = 1e-2*np.ones(n_points)*np.sin(helix_angle)
        Q_z = np.zeros(n_points)
        wear_data = pd.DataFrame({'loc_x': np.zeros(n_points),
                                  'loc_y': y,
                                  'loc_z': np.ones(n_points),
                                  'Q_x': Q_x,
                                  'Q_y': Q_y,
                                  'Q_z': Q_z})
        wear_data['Q'] = wear_data[['Q_x', 'Q_y', 'Q_z']].apply(np.linalg.norm, axis=1)
        self.shell.wear_data = wear_data
        self.shell.apply_wear(patch_size_factor=1)

        # Get worn volume
        worn_vol = self.shell.get_volume()
        
        # Get Calculated Volume Change
        calculated_total_wear = self.shell.wear_data['Q'].sum()

        # Get Actual Volume Change
        actual_volume_change = unworn_vol-worn_vol
        print(actual_volume_change, calculated_total_wear)
        # Compare
        self.assertAlmostEqual(calculated_total_wear, actual_volume_change, places=4)

    def tearDown(self):
        return

class Test_Leadscrew(unittest.TestCase):

    def setUp(self):
        for mod in Adams.Models.values():
            mod.destroy()

        mod = Adams.Models.create()
        leadscrew: Part = mod.Parts.createRigidBody(name='leadscrew')

        self.screw = leadscrew.Geometries.createShell(file_name=str(RESOURCES / 'leadscrew.shl'),
                                                      ref_mkr=leadscrew.Markers.create(name='ref_mkr'))

        sys.path.insert(0, 'C:\\Users\\ben.thornton\\Hexagon\\NNL - Roller Nut Drive - Engineering\\plugin\\working_directory\\modules\\qual\\utilities\\wear\\leadscrew')
        from mock import make_fake_wear_file, TOTAL_WEAR
        set_dv(self.screw.parent, 'ls_major_diam', 1.625)
        set_dv(self.screw.parent, 'ls_pitch_diam', 1.5)
        set_dv(self.screw.parent, 'ls_minor_diam', 1.365)
        set_dv(self.screw.parent, 'ls_top_flank', 1)
        set_dv(self.screw.parent, 'ls_bot_flank', 3)
        set_dv(self.screw.parent, 'ls_pitch', 0.5)
        set_dv(self.screw.parent, 'ls_tooth_width', 0.25)
        set_dv(self.screw.parent, 'ls_threaded_length', 25)
        set_dv(self.screw.parent, 'ls_internal_diam', 0.875)
        set_dv(self.screw.parent, 'ls_unthreaded_diam', 1.625)
        set_dv(self.screw.parent, 'ls_unthreaded_length_top', 1)
        set_dv(self.screw.parent, 'ls_unthreaded_length_bot', 10)
        set_dv(self.screw.parent, 'ls_mass', 8.201)
        set_dv(self.screw.parent, 'ls_IXX', 428.728)
        set_dv(self.screw.parent, 'ls_IYY', 428.728)
        set_dv(self.screw.parent, 'ls_IZZ', 3.187)
        set_dv(self.screw.parent, 'ls_IXY', 0)
        set_dv(self.screw.parent, 'ls_IZX', 0)
        set_dv(self.screw.parent, 'ls_IYZ', 0)
        set_dv(self.screw.parent, 'ls_vert_dist', 10)
        set_dv(self.screw.parent, 'ls_axial_rotation', -145)
        set_dv(self.screw.parent, 'ls_stop_vert_dist', 41.7)
        set_dv(self.screw.parent, 'ls_attached_mass', 10)
        set_dv(self.screw.parent, 'ls_attached_mass_offset', 0)
        set_dv(self.screw.parent, 'ls_attached_mass_radius', 2)
        set_dv(self.screw.parent, 'ls_helix_angle', 6.0767155072)
        make_fake_wear_file(self.screw, TOTAL_WEAR)


        self.shell = WearableShell(self.screw)

    def test_leadscrew(self):

        wear_data = pd.read_pickle(Path(self.screw.file_name).with_suffix('.wear'))

        # Get unworn volume
        unworn_vol = self.shell.get_volume()

        self.shell.wear_data = wear_data
        self.shell.apply_wear(patch_size_factor=1)

        # Get worn volume
        worn_vol = self.shell.get_volume()
        
        # Get Calculated Volume Change
        calculated_total_wear = self.shell.wear_data['Q'].sum()

        # Get Actual Volume Change
        actual_volume_change = unworn_vol-worn_vol
        print(actual_volume_change, calculated_total_wear)
        # Compare
        self.assertAlmostEqual(calculated_total_wear, actual_volume_change, places=4)

    def tearDown(self):
        return


def make_cube_shell(ref_mkr: Marker, edge_length=1, name=None):
    """Make a cube shell"""
    with pygmsh.geo.Geometry() as geom:
        geom.add_box(0, edge_length, 0, edge_length, 0, edge_length, mesh_size=0.5)

        mesh = geom.generate_mesh()

    points = mesh.points
    facets = np.array(mesh.cells[1].data, dtype=np.int32)

    facets = fix_box_normals(points, facets)

    write_shell_file(points, facets, RESOURCES / 'cube_shell.shl', scale=.0254)

    part: Part = ref_mkr.parent
    cube = part.Geometries.createShell(file_name=str(RESOURCES / 'cube_shell.shl'),
                                       reference_marker=ref_mkr,
                                       name=name)

    return cube

def make_long_rect_shell(ref_mkr: Marker, edge_length=1, name=None):
    """Make a long rectangle shell"""
    with pygmsh.geo.Geometry() as geom:
        geom.add_box(0, edge_length, 0, edge_length*2, 0, edge_length, mesh_size=0.5)

        mesh = geom.generate_mesh()

    points = mesh.points
    facets = np.array(mesh.cells[1].data, dtype=np.int32)

    facets = fix_box_normals(points, facets)

    write_shell_file(points, facets, RESOURCES / 'long_rect_shell.shl', scale=.0254)

    part: Part = ref_mkr.parent
    long_rect = part.Geometries.createShell(file_name=str(RESOURCES / 'long_rect_shell.shl'),
                                       reference_marker=ref_mkr,
                                       name=name)

    return long_rect

def make_the_rest_of_the_model(mod, box_geom):
    sphere_part: Part = mod.Parts.createRigidBody(name='sphere', density=.28)
    sphere_cntr_mkr = sphere_part.Markers.create(name='center_mkr')
    sphere_geom = sphere_part.Geometries.createEllipsoid(name='sphere_geom',
                                                            center_marker=sphere_cntr_mkr)
    mod.Contacts.createSolidToSolid(i_geometry=box_geom,
                                    j_geometry=sphere_geom,
                                    stiffness=1e6,
                                    damping=1e4,
                                    dmax=0.1,
                                    exponent=1.2)
    mod.Forces.createSingleComponentForce(name='force',
                                            i_marker=sphere_part.cm,
                                            j_marker=mod.ground_part.Markers.create(name='j_mkr'),
                                            action_only=True,
                                            function="10*sin(2*pi*time)")

def fix_box_normals(points, facets):
    points = np.array(points, dtype=np.float64)
    facets = np.array(facets, dtype=np.int32)
    cm = np.mean(points, axis=0)
    for idx, facet in enumerate(facets):
        normal = get_normal_of_points(points[facet])
        cm_f = np.mean(points[facet], axis=0)
        cm_to_facet = cm_f - cm
        if np.dot(cm_to_facet, normal) < 0:
            facets[idx] = facet[::-1]

    return facets

def get_normal_of_points(points):
    """ Returns the normal of a collection of points in a plane.
    
    Parameters
    ----------
    points : List[Point]
        Points to find the plane of
        
    Returns
    -------
    Tuple[float, float, float]
        Unit vector normal to the plane that contains the points
    """
    points = np.array(points)
    p1, p2, p3 = points[0], points[1], points[2]
    # Loop over all triples of points

    # Get the normal vector of the plane
    normal = np.cross(np.array(p2)-np.array(p1), np.array(p3)-np.array(p1))


    # Return the normalized vector
    return normal / np.linalg.norm(normal)

    