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

    a = []
    col = True
    for i in range(len(path)):
        if i == 0:
            a += [(0.0, 0.0, 1.0, 1.0)]
        elif col:
            a += [(1.0, 0.0, 0.0, 1.0)]
        else:
            a += [(0.0, 1.0, 0.0, 1.0)]
        col = not col
    line1 = scene.visuals.Line(pos = path.copy(),
                               method = 'gl',
                               antialias=True,
                               name='line1',
                               color=a,
                               parent=vb.scene,
                               connect='strip')

    ax = scene.visuals.XYZAxis(name='test', parent=vb)
    app.run()

def smooth(a, c=100):
    return np.convolve(a, np.ones(c)/c, mode='same')
def random_path(n):
    steps = np.random.random_integers(1, 10, n)/10
    directions = np.random.uniform(0, 2 * np.pi, n)
    directions = smooth(directions)
    floor_dir = ((np.random.uniform(0,1,n) > 0.5).astype(np.float32)*2 - 1)
    change_floor = np.random.uniform(0,1,n) > 0.9
    floor_dir[~change_floor] = 0.0
    floor_dir *= 0.1
    return np.c_[steps, directions, floor_dir]

def stair_case(n):
    directions = np.zeros(n)
    steps = np.ones(n) * 0.1
    change_in_height = np.round(np.linspace(0,1,n),1)
    return np.c_[steps, directions, change_in_height]

def spiral_stair_case(n, r):
    directions = np.linspace(0,r*(2*np.pi)*100, n) % (2 * np.pi)
    steps = np.ones(n) * 0.01
    change_in_height = np.round(np.linspace(0,0.5,n),1)
    return np.c_[steps, directions, change_in_height]

def position(path):
    change_x = path[:, 0] * np.cos(path[:, 1])
    change_y = path[:, 0] * np.sin(path[:, 1])
    change_z = path[:, 2]

    
    path_x = np.cumsum(change_x)
    path_y = np.cumsum(change_y)
    path_z = np.cumsum(change_z)

    data =  np.c_[path_x, path_y, path_z]
    z = np.zeros((1,3))
    return np.concatenate([z, data], axis=0)
