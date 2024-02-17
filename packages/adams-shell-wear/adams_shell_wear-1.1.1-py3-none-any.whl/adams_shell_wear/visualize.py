import webbrowser
from pathlib import Path
from tempfile import NamedTemporaryFile

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from aviewpy.cs import cart_to_cyl

from .utils.shell_file import get_shell_diff_vectors

MKR_PROPS = dict(
    colorscale='Viridis',
    colorbar=dict(
        thickness=20,
        len=.25,
        x=0,
        y=.8,
        xanchor='right',
        title=dict(
            text='Nodal Deformation (in)',
            side='top',
        ),
        ticklabelposition='inside left',
        tickformat='.2e',
        ticks='outside',
    ),
    size=10,
    symbol='circle',
)
HOVER_TEMPLATE = (
    '<b>Location</b><br>' + 
    '<b>x</b>: %{customdata[0]:1.2e}<br>' +
    '<b>y</b>: %{customdata[1]:1.2e}<br>' +
    '<b>z</b>: %{customdata[2]:1.2e}<br>' +
    '<br><b>Nodal Deformations</b><br>' + 
    '<b>dmag</b>: %{customdata[3]:1.2e}<br>' +
    '<b>dx</b>: %{customdata[4]:1.2e}<br>' +
    '<b>dy</b>: %{customdata[5]:1.2e}<br>' +
    '<b>dz</b>: %{customdata[6]:1.2e}<br>' +
    '<b>dr</b>: %{customdata[7]:1.2e}<br>' +
    '<extra></extra>'
)

CAMERA = dict(
    projection={'type': 'orthographic'},
    # center={'x': 0, 'y': 0, 'z': 0},
)



def plot_wear(vectors: pd.DataFrame, nodes: pd.DataFrame):
    """Plots the wear vectors as colored points overlaied on the leadscrew points.

    Parameters
    ----------
    vectors : pd.DataFrame
        `DataFrame` with 'mag', 'd_x', 'd_y', 'd_z'
    nodes : pd.DataFrame
        `DataFrame` with x, y, z

    Returns
    -------
    Plotly Figure
    """
    for col in ('x', 'y', 'z'):
        vectors[col.upper()] = nodes[col] + vectors[f'd_{col}']
    r_unworn, _, _ = cart_to_cyl(*nodes[['x', 'y', 'z']].values.T)
    r_worn, _, _ = cart_to_cyl(*vectors[['X', 'Y', 'Z']].values.T)
    vectors['d_r'] = r_worn - r_unworn
    vectors['mag'] = vectors[['d_x', 'd_y', 'd_z']].apply(np.linalg.norm, axis=1)

    custom_data = np.stack((
        vectors['X'],
        vectors['Y'],
        vectors['Z'],
        vectors['mag'],
        vectors['d_x'],
        vectors['d_y'],
        vectors['d_z'],
        vectors['d_r'],
    ), axis=-1)

    common_props = dict(
        mode='markers',
        customdata=custom_data,
        hovertemplate=HOVER_TEMPLATE,
        opacity=1,
        showlegend=False
    )

    fig = (go.Figure(data=[
        go.Scatter3d(
            x=nodes.x,
            y=nodes.y,
            z=nodes.z,
            mode='markers',
            marker=dict(
                color='rgb(110, 110, 110)',
                size=2,
                symbol='circle',
            ),
            opacity=0.5,
            hovertemplate=('<b>x</b>: %{x:1.2f}<br>' +
                        '<b>y</b>: %{y:1.2f}<br>' +
                        '<b>z</b>: %{z:1.2f}<br>' +
                        '<extra></extra>')
            # name='Original Mesh',
        ),
        go.Scatter3d(
            x=vectors.X,
            y=vectors.Y,
            z=vectors.Z,
            marker=dict(
                color=vectors.mag,
                **MKR_PROPS,
            ),
            name='Nodal Deformation Magnitude',
            **common_props
        ),
        go.Scatter3d(
            x=vectors.X,
            y=vectors.Y,
            z=vectors.Z,
            marker=dict(
                color=vectors.d_x,
                **MKR_PROPS,
            ),
            visible=False,
            name='X Nodal Deformation',
            **common_props,
        ),
        go.Scatter3d(
            x=vectors.X,
            y=vectors.Y,
            z=vectors.Z,
            marker=dict(
                color=vectors.d_y,
                **MKR_PROPS,
            ),
            visible=False,
            name='Y Nodal Deformation',
            **common_props,
        ),
        go.Scatter3d(
            x=vectors.X,
            y=vectors.Y,
            z=vectors.Z,
            marker=dict(
                color=vectors.d_z,
                **MKR_PROPS,
            ),
            visible=False,
            name='Z Nodal Deformation',
            **common_props,
        ),
        go.Scatter3d(
            x=vectors.X,
            y=vectors.Y,
            z=vectors.Z,
            marker=dict(
                color=vectors.d_r,
                **MKR_PROPS,
            ),
            visible=False,
            name='R Nodal Deformation',
            **common_props,
        )
    ])
    .update_scenes(aspectmode='data', aspectratio=dict(x=1, y=1, z=1))
    .update_layout(
        template='seaborn',
        scene=dict(zaxis=dict(dtick=1)),
        scene_camera=CAMERA,
        # width=2000, height=1000,
        showlegend=False,
        updatemenus=[
            go.layout.Updatemenu(
                active=0,
                buttons=list(
                    [dict(label='Magnitude',
                          method='update',
                          args=[
                              {'visible': [True, True, False, False, False, False]}]),
                     dict(label='x',
                          method='update',
                          args=[
                              {'visible': [True, False, True, False, False, False]},
                          ]),
                     dict(label='y',
                          method='update',
                          args=[
                              {'visible': [True, False, False, True, False, False]},
                          ]),
                     dict(label='z',
                          method='update',
                          args=[
                              {'visible': [True, False, False, False, True, False]},
                          ]),
                     dict(label='r',
                          method='update',
                          args=[
                              {'visible': [True, False, False, False, False, True]},
                          ]),
                     ])
            ),
            # go.layout.Updatemenu(
            #     active=0,
            #     buttons=list(
            #         [dict(label='Light Mode',
            #               method='relayout',
            #               args=[{'template': 'plotly'}]),
            #          dict(label='Dark Mode',
            #               method='relayout',
            #               args=[{'template': 'plotly_dark'}])
            #          ]
            #     )
        ])
    )

    return fig


def visualize(nodes, vectors):
    """
    Visualize the wear on a shell.
    
    Parameters
    ----------
    nodes : array_like
        The nodes of the shell.
        
    vectors : array_like
        The vectors representing the wear on the shell.
    """
    fig = plot_wear(pd.DataFrame(vectors, columns=('d_x', 'd_y', 'd_z')),
                    pd.DataFrame(nodes, columns=('x', 'y', 'z')))

    with NamedTemporaryFile(delete=False, mode='w', suffix='.html') as fid:
        html_file = Path(fid.name)
        fid.write(fig.to_html(config={'displaylogo': False}))
    
    webbrowser.open_new_tab(html_file)


def visualize_from_files(shell_file_1: Path, shell_file_2: Path, scale_factor: float = 1.0):
    """
    Visualize the wear on a shell.

    Parameters
    ----------
    shell_file_1 : Path
        The path to the first shell file.

    shell_file_2 : Path
        The path to the second shell file.
    """
    df = (get_shell_diff_vectors(shell_file_1, shell_file_2)
          .rename(columns={'x_1': 'x', 'y_1': 'y', 'z_1': 'z'}))
          
    visualize(df[['x', 'y', 'z']].values, df[['d_x', 'd_y', 'd_z']].values*scale_factor)
