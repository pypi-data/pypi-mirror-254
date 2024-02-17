"""Genearl utilities module"""
from pathlib import Path
from typing import List

import numpy as np
from numpy.typing import ArrayLike, NDArray

from .plane import project_to_plane


def wrap_angle(theta: ArrayLike, limit=np.pi) -> NDArray:
    """Converts angles to +/- `limit`z

    Parameters
    ----------
    theta : ArrayLike
        Angles
    limit : float, optional
        Absolute values will not exceed this value, by default `np.pi`

    Returns
    -------
    NDArray
        Wrapped angles
    """
    return (theta + limit) % (2 * limit) - limit


def unique_path(filename: Path):
    filename = Path(filename)

    try:
        idx = int(filename.stem.split('_')[-1])
        stem = '_'.join(filename.stem.split('_')[:-1])
    except ValueError:
        idx = 1
        stem = filename.stem

    while filename.exists():
        filename = filename.with_name(stem + f'_{idx}{filename.suffix}')
        idx += 1

    return filename


def three_point_area(p1: ArrayLike, p2: ArrayLike, p3: ArrayLike, in_plane: List[float] = None) -> float:
    """Calculates the area of a triangle given three points in 3D space

    Parameters
    ----------
    p1 : ArrayLike
        Point 1
    p2 : ArrayLike
        Point 2
    p3 : ArrayLike
        Point 3
    in_plane : List[float], optional
        A plane that the points should be projected to before calculating the area, 
        by default None

    Returns
    -------
    float
        Area of triangle
    """
    if in_plane is not None:
        cg = np.mean([p1, p2, p3], axis=0)
        p1 = p1 - cg
        p2 = p2 - cg
        p3 = p3 - cg
        p1 = project_to_plane(p1, in_plane)
        p2 = project_to_plane(p2, in_plane)
        p3 = project_to_plane(p3, in_plane)

    v1 = np.array(p1) - np.array(p2)
    v2 = np.array(p3) - np.array(p2)
    return 0.5 * np.linalg.norm(np.cross(v1, v2))
