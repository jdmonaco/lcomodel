#!/usr/bin/env python
#encoding: utf-8

# In[65]:

from __future__ import division, print_function


# ## Loading tracking data from Blair lab test data set
# 
# We need to get some tracking data to run the toy model simulation on. We will use a short segment of the Blair test data set, but long enough to at least coarsely visit most locations in the environment. 
# 
# The data is stored in MATLAB files, so we need MATLAB loading functions.

# In[66]:

import scipy.io as sio


# ## Directory structure
# 
# The test data set for rat 10 day 8 is located under the root folder `~/theta-data/`.

# In[67]:

import os
root = '/Users/joe/theta-data/'
dataset = os.path.join(root, 'OTheta10/OTheta10_Day8')
assert os.path.isdir(dataset)


# ## Load the tracking data
# 
# Load the `trackdata.mat` file into the workspace.

# In[68]:

tracking_file = os.path.join(dataset, 'trackdata.mat')
trackdata = sio.loadmat(tracking_file)


# In[69]:

print(*sorted(trackdata.keys()), sep=', ')


# In[78]:

start = 30.0 # s
duration = 300.0 # s
fs = 30.0 # s
res = 4.0 # pixels/cm

t0 = int(start * fs)
N = int(duration * fs)
t_slice = slice(t0, t0 + N)

print('Starting at sample %d for a total of %d samples.' % (t0, N))


# In[80]:

x, t = trackdata['Position_X'][t_slice].T
y = trackdata['Position_Y'][t_slice,0]
print('Data starts at t = %f.' % t[0])

# Convert from pixels to cm
x /= res
y /= res

import numpy as np
pos = np.c_[t, x, y].T
print('New position shape = ', pos.shape)


# ## Plot the tracking data segment
# 
# Using matplotlib inline

# In[72]:

get_ipython().magic(u'matplotlib osx')
import matplotlib.pyplot as plt


# In[81]:

plt.plot(x, y, 'k-', alpha=0.7)
plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')


# ## Save the tracking segment
# 
# Store the data as numpy array in modeling data subdirectory.
# 

# In[74]:

model_path = '/Users/joe/source/phase_model'
data_path = os.path.join(model_path, 'data')
assert os.path.isdir(data_path)


# In[82]:

save_file = os.path.join(data_path, 'pos.npy')
np.save(save_file, pos)
print('Saved:', save_file)


# Position data file pos.npy is a row-wise matrix of time, x-position, and y-position.

# ## Verify the saved tracking data
# 
# Load the saved binary array data from the model directory to verify. 

# In[84]:

pos_saved = np.load(save_file)
plt.plot(pos_saved[1], pos_saved[2], 'b-', alpha=0.7)
plt.axis('equal')


# In[ ]:



