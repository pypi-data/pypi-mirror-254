
from pathlib import Path

import Adams  # type:ignore # noqa
import matplotlib.pyplot as plt
import numpy as np
from Geometry import GeometryShell  # type:ignore # noqa

WORK_DIR = Path('C:/Users/ben.thornton/Hexagon/NNL - Roller Nut Drive - Engineering',
                   'plugin/working_directory')


mod = Adams.getCurrentModel()

if 'leadscrew' not in mod.Parts:
    ls = mod.Parts.createRigidBody(name='leadscrew')
else:
    ls = mod.Parts['leadscrew']

ref_mkr = ls.Markers.create()

if 'screw' not in ls.Geometries:
    screw: GeometryShell = ls.Geometries.createShell(
        name='screw',
        reference_marker=ref_mkr,
        file_name=str(list(WORK_DIR.glob('leadscrew*.shl'))[-1])
    )
else:
    screw = ls.Geometries['screw']

points = np.array(screw.points)
connections = np.array(screw.connections)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

for connection in connections[:1]:
    for el in zip(connection[::2], connection[1::2], connection[2::2]):
        ax.plot(*points[list(el)+[el[0]]].T, alpha=.5)

# ax.scatter(*points.T, s=1, c='k', alpha=.25)

ax.axis('square')

plt.show()
