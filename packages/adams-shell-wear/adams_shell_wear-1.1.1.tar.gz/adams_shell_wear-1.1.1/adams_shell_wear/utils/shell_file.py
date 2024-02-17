from pathlib import Path

import pandas as pd
from aviewpy.files.shell import read_shell_file
from scipy.spatial import KDTree


def get_shell_diff_vectors(file_1: Path, file_2: Path):
    """Get a vector of the differences between two (.shl) files

    Parameters
    ----------
    file_1 : Path
        Full path of shell file 1
    file_2 : Path
        Full path of shell file 2

    Returns
    -------
    bool
        True if the two files are the same
    """
    points_1, _ = read_shell_file(file_1)
    points_2, _ = read_shell_file(file_2)

    # Match each point in points_1 to the closest point in points_2 and create a dataframe of the distance components
    df = pd.DataFrame(points_1, columns=['x_1', 'y_1', 'z_1'])
    
    df['idx_pt_2'] = KDTree(points_2).query(points_1)[1]
    df[['x_2', 'y_2', 'z_2']] = df['idx_pt_2'].apply(lambda idx: points_2[idx]).tolist()

    df[['d_x', 'd_y', 'd_z']] = df[['x_1', 'y_1', 'z_1']].to_numpy() - df[['x_2', 'y_2', 'z_2']].to_numpy()
    
    return df
