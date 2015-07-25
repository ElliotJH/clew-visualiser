from vispy import app
from vispy import scene

import numpy as np

def visualise_path(path):
    canvas = scene.SceneCanvas(show=True, keys='interactive')
    grid = canvas.central_widget.add_grid()
    
    vb = grid.add_view(name='vb')
    vb.parent = canvas.scene
    vb.clip_method='viewport'
    vb.camera = scene.TurntableCamera(elevation=30, azimuth=30, up='+z')

    line1 = scene.visuals.Line(pos = path.copy(),
                               method = 'gl',
                               antialias=True,
                               name='line1',
                               color=(0.8, 0.4, 0.4, 1),
                               parent=vb.scene)

    ax = scene.visuals.XYZAxis(name='test', parent=vb)
    app.run()

def smooth(a, c=100):
    return np.convolve(a, np.ones(c)/c, mode='same')
def random_path(n):
    steps = np.random.random_integers(1, 10, n)/10
    directions = np.random.uniform(0, 2 * np.pi, n)
    directions = smooth(directions)
    change_in_elevation  = smooth(np.random.uniform(0, 0.01, n))
    
    return np.c_[steps, directions, change_in_elevation]

def position(path):
    change_x = path[:, 0] * np.cos(path[:, 1])
    change_y = path[:, 0] * np.sin(path[:, 1])
    change_z = path[:, 2]

    path_x = np.cumsum(change_x)
    path_y = np.cumsum(change_y)
    path_z = np.cumsum(change_z)

    return np.c_[path_x, path_y, path_z]
    
visualise_path(position(random_path(500)))