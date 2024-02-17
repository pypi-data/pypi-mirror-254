from typing import List
import numpy as np
from scipy.linalg import lstsq
from numpy.typing import NDArray, ArrayLike

def fit_plane(points: NDArray):
    """Find the plane that best fits `points`.

    Assumes a plane is defined as:
        z = a*x + b*y + c

    Alternative form:
        lx + my + nz = d
        (l/d)*x + (m/d)*y + (n/d)*z = 1
        z = (-l/n)*x + (-m/n)*y + d/n
    
    Conversion between the two forms
    * a = (-l/n)
    * b = (-m/n)
    * c = d/n   

    * l = -a*(d/c)
    * m = -b*(d/c)
    * n = d/c   


    Parameters
    ----------
    points : NDArray
        Nx3 array of points

    Returns
    -------
    tuple
        The planar coefficients (a, b, c, d)
    """
    A = np.c_[points[:,0], points[:,1], np.ones(points.shape[0])]
    coeffs, *_ = lstsq(A, points[:,2])    

    return coeffs

def plane_normal_from_coeffs(coeffs: ArrayLike)->NDArray:
    """Returns a unit vector normal to the plane defined by :arg:`coeffs

    Parameters
    ----------
    coeffs : ArrayLike
        Plane coefficients (array of length 3)

    Returns
    -------
    NDArray
        unit vector normal to the plane defined by :arg:`coeffs
    """
    # create three points on the plane
    x = np.array([0, 0, 1])
    y = np.array([0, 1, 0])
    z: NDArray = coeffs[0]*x + coeffs[1]*y + coeffs[2]

    unit = plane_normal_from_points(*np.array([x, y, z]).T)

    return unit

def plane_normal_from_points(q:NDArray, r:NDArray, s:NDArray):
    """Returns a unit vector normal to the plane defined by the three points given.

    Parameters
    ----------
    q : NDArray
    r : NDArray
    s : NDArray

    Returns
    -------
    NDArray
        unit vector normal to the plane defined by the three points given
    """
    normal = np.cross(r - q, s - q)
    unit = normal/np.linalg.norm(normal)

    # Always give it in positive x-dir unless x is zero, then give it in positive y dir
    if unit[0] < 0 or (unit[0] == 0 and unit[1] < 0):
        unit = -unit

    return unit

def project_to_plane(point: List[float], plane_normal: List[float]):
    """Project a point onto a plane defined by a normal vector

    Parameters
    ----------
    point : List[float]
        Point to project
    plane_normal : List[float]
        Normal vector to plane

    Returns
    -------
    List[float]
        Point projected onto plane
    """
    point = np.array(point, dtype=float)
    plane_normal = np.array(plane_normal, dtype=float)

    return point - np.dot(point, plane_normal)*plane_normal
