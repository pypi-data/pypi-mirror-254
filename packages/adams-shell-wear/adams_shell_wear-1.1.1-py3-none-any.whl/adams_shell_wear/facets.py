from typing import List, Tuple
import numpy as np
from numpy.typing import ArrayLike, NDArray


def face_cms(face, points):
    points_a, points_b, points_c = np.array(list(zip(face[:-2], face[1:-1], face[2:]))).T

    cms_x = np.mean(
        np.array([points[points_a, 0], points[points_b, 0], points[points_c, 0]]), axis=0)
    cms_y = np.mean(
        np.array([points[points_a, 1], points[points_b, 1], points[points_c, 1]]), axis=0)
    cms_z = np.mean(
        np.array([points[points_a, 2], points[points_b, 2], points[points_c, 2]]), axis=0)
    return np.array([cms_x, cms_y, cms_z]).T


def angle_between(vec_a: ArrayLike, vec_b: ArrayLike) -> float:
    """Returns the angle in radians between vectors `vec_a` and `vec_b`

    Parameters
    ----------
    vec_a : ArrayLike
        Vector A
    vec_b : ArrayLike
        Vector B
    
    Returns
    float
        Angle between the two vectors
    """
    unit_a = vec_a/np.linalg.norm(vec_a)
    unit_b = vec_b/np.linalg.norm(vec_b)
    return np.arccos(np.clip(np.dot(unit_a, unit_b), -1.0, 1.0))


def get_coincident_points(idx_point, points) -> List[int]:
    """Gets all points that are coincident to `idx_point`

    Parameters
    ----------
    idx_point : int
        The index of the point for which coincident points should be found
    
    points : List[List[float]]
        A list of points

    Returns
    -------
    List[int]
        List of indices of points that are coincident to `idx_point`
    """
    return [i_pt for i_pt in range(len(points))
            if points[i_pt] == points[idx_point]]


def normal_at_point(face: ArrayLike, idx_point: int, points: List[Tuple[float, float, float]]):
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
    face = np.array(face)

    idx_coinc_points = get_coincident_points(idx_point, points)

    # Find the face index of the point that is actually on `face`
    iface_pt = list(face).index(next(idx for idx in idx_coinc_points if idx in face))

    if len(face) > 3:

        # Build the index array for all facets on the face that contain idx_point
        iface_a = np.arange(max(0, iface_pt-2), min(len(face)-3, iface_pt+2)+1)
        iface_b = iface_a+1
        iface_c = iface_a+2

    elif len(face) == 3:
        iface_a = np.array([iface_pt])
        iface_b = (iface_a+1) % len(face)
        iface_c = (iface_a+2) % len(face)

    ipts_a: NDArray = face[iface_a]
    ipts_b: NDArray = face[iface_b]
    ipts_c: NDArray = face[iface_c]

    vecs_ab = np.array(points)[ipts_a] - np.array(points)[ipts_b]
    vecs_ac = np.array(points)[ipts_a] - np.array(points)[ipts_c]
    normals = np.cross(vecs_ab, vecs_ac)

    # Ensure that the x component is positive
    # TODO: What if x is zero?
    normals = np.apply_along_axis(flip, 1, normals)

    mean_normal = normals.mean(axis=0)
    return mean_normal/np.linalg.norm(mean_normal)

def flip(xyz):
    if xyz[0] > 0:
        return xyz
    elif xyz[0] < 0:
        return -xyz
    elif xyz[1] > 0:
        return xyz
    elif xyz[1] < 0:
        return -xyz
    elif xyz[2] > 0:
        return xyz
    elif xyz[2] < 0:
        return -xyz
    else:
        return xyz
