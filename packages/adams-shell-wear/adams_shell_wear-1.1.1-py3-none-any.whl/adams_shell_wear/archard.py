import numpy as np
import pandas as pd
from scipy.integrate import cumtrapz, trapz
from thornpy.signal import resample_dataframe_non_time
from numpy.typing import ArrayLike, NDArray

def wear_rate(W: ArrayLike, v_slide: ArrayLike, K_d: float) -> NDArray:
    """Returns the rate of material removal

    Parameters
    ----------
    W : ArrayLike
        Normal force
    v : ArrayLike
        Sliding velocity
    K_d : float
        Dimensional wear coefficent

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
    return abs(K_d*np.array(W)*np.array(v_slide))


def wear_volume(dQ: ArrayLike, time: ArrayLike) -> pd.Series:
    """Returns the total volume of material removed

    Parameters
    ----------
    dQ : ArrayLike
        Wear rate
    time : ArrayLike
        Time array to which :arg:`dQ` is indexed

    Returns
    -------
    pd.Series
        Cumulative wear as a function of time
    """
    if len(dQ) > 0:
        Q = pd.Series(cumtrapz(dQ, time, initial=0), index=time)
    
    else:
        Q = pd.Series([0], index=time)
    
    return Q


def instantaneous_wear_volume(dQ, time) -> pd.Series:
    """Returns the instantaneous volume of material removed

    Parameters
    ----------
    dQ : ArrayLike
        Wear rate
    time : ArrayLike
        Time array to which :arg:`dQ` is indexed

    Returns
    -------
    pd.Series
        Cumulative wear as a function of time
    """
    if len(dQ) == 0:
        Q = pd.Series([0], index=time)

    else:
        df = pd.DataFrame({'dQ': dQ, 'time': time})
        Q = [0] + [trapz(df.iloc[i-1:i+1]['dQ'].values, df.iloc[i-1:i+1]['time'])
                   for i in range(1, len(df))]
        Q = pd.Series(Q, index=time)

    return Q