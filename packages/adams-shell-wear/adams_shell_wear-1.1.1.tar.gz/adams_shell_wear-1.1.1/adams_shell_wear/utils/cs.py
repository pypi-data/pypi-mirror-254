from __future__ import annotations
from typing import Union

import Adams  # type: ignore # noqa
import numpy as np
from Analysis import Analysis  # type: ignore # noqa
from Marker import Marker  # type: ignore # noqa
from Part import Part  # type: ignore # noqa
from scipy.spatial.transform import Rotation as R


class CS():
    def __init__(self, loc, ori=None, design_loc=None, design_ori=None):
        self.loc = loc
        self.ori = ori
        self.design_loc = design_loc if design_loc is not None else loc[0]
        self.design_ori = design_ori if design_ori is not None else (ori[0]
                                                                     if ori is not None
                                                                     else None)

    def __add__(self, other: CS) -> CS:
        rot = self.rot * other.rot
        design_rot = self.design_rot * other.design_rot
        return CS(
            loc=self.loc + other.loc,
            ori=rot.as_euler('ZXZ', degrees=True),
            design_loc=self.design_loc + other.design_loc,
            design_ori=design_rot.as_euler('ZXZ', degrees=True),
        )

    def __sub__(self, other: CS) -> CS:

        if other.rot is not None and self.rot is not None:
            rot: R = other.rot.inv() * self.rot
            ori=rot.as_euler('ZXZ', degrees=True)
            design_rot: R = (self.design_rot * other.design_rot.inv())
            design_ori=design_rot.as_euler('ZXZ', degrees=True)
        
        else:
            ori = None
            design_ori = None
        
        return CS(
            loc=self.loc - other.loc,       
            ori=ori,
            design_loc=self.design_loc - other.design_loc,
            design_ori=design_ori,
        )

    @property
    def rot(self) -> Union[R, None]:
        if self.ori is not None:
            return R.from_euler('ZXZ', self.ori, degrees=True) 
        else:
            return None

    @property
    def design_rot(self) -> Union[R, None]:
        if self.design_ori is not None: 
            return R.from_euler('ZXZ', self.design_ori, degrees=True)
        else:
            return None


class PartCS(CS):

    def __init__(self, part: Part, ans: Analysis):
        design_loc = np.array(Adams.evaluate_exp(f'loc_global({{0,0,0}}, {part.full_name})'))
        design_ori = np.array(Adams.evaluate_exp(f'ori_global({{0,0,0}}, {part.full_name})'))
        loc = np.array([Adams.evaluate_exp(f'{ans.full_name}.{part.name}_XFORM.{d}.values')
                        for d in ('X', 'Y', 'Z')]).T
        ori = np.array([Adams.evaluate_exp(f'{ans.full_name}.{part.name}_XFORM.{d}.values')
                        for d in ('PSI', 'THETA', 'PHI')]).T

        super().__init__(loc, ori, design_loc, design_ori)


class MarkerCS(CS):

    def __init__(self, mkr: Marker, ans: Analysis):
        design_loc = np.array(Adams.evaluate_exp(f'loc_global({{0,0,0}}, {mkr.full_name})'))
        design_ori = np.array(Adams.evaluate_exp(f'ori_global({{0,0,0}}, {mkr.full_name})'))

        part_gcs = PartCS(mkr.parent, ans)

        rel_loc = design_loc-part_gcs.design_loc
        loc = part_gcs.loc+rel_loc
        rot: R = part_gcs.rot * R.from_euler('ZXZ', mkr.orientation, degrees=True)
        ori = rot.as_euler('ZXZ', degrees=True)

        super().__init__(loc, ori, design_loc, design_ori)
