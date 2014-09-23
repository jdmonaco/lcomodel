# coding: utf-8

"""
Script to load an example trajectory from the Blair lab datasets
"""

from __future__ import division, print_function

import os
import scipy.io as sio
import matplotlib.pyplot as plt

root = '/Users/joe/data/blab/'
dataset = os.path.join(root, 'OTheta10/OTheta10_Day8')

model_path = '/Users/joe/source/phase_model'
data_path = os.path.join(model_path, 'data')
save_file = os.path.join(data_path, 'pos.npy')

start = 30.0 # s
duration = 300.0 # s
fs = 30.0 # s
res = 5.5 # pixels/cm


def load_raw():
    assert os.path.isdir(dataset)
    tracking_file = os.path.join(dataset, 'trackdata.mat')
    trackdata = sio.loadmat(tracking_file)
    print('Loaded tracking data from', tracking_file, '.')
    return trackdata

def trajectory(data=None):
    if data is None:
        data = load_raw()

    t0 = int(start * fs)
    N = int(duration * fs)
    t_slice = slice(t0, t0 + N)

    print('Starting at sample %d for a total of %d samples.' % (t0, N))

    x, t = trackdata['Position_X'][t_slice].T
    y = trackdata['Position_Y'][t_slice,0]

    print('Data starts at t = %f.' % t[0])

    # Convert from pixels to cm
    x /= res
    y /= res

    traj = np.c_[t, x, y].T
    return traj

def plot(traj=None):
    if traj is None:
        traj = trajectory()
    t, x, y = traj

    plt.plot(x, y, 'k-', alpha=0.7)
    plt.axis('equal')
    plt.xlabel('x')
    plt.ylabel('y')

def save(traj=None):
    if traj is None:
        traj = trajectory()

    if not os.path.isdir(data_path):
        os.makedirs(data_path)
    np.save(save_file, traj)
    print('Saved:', save_file)

def load():
    return np.load(save_file)

def load_trajectory():
    pos_saved = np.load(save_file)
    plt.plot(pos_saved[1], pos_saved[2], 'b-', alpha=0.7)
    plt.axis('equal')
