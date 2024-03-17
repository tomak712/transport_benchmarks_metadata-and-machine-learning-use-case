#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 15:46:03 2023

@author: thomasking
"""

import h5py
import numpy as np
import math
import keras
from sklearn.model_selection import train_test_split

f = h5py.File('plane_IC.hdf5')



er babykeys = []
values = []
time = []
sols = []

items = f['plane_IC'].items()
for item in items:
    keys.append(item[0]), values.append(item[1])
    
for i in range(len(keys)):
    keys[i] = keys[i][4:]
    time.append(float(keys[i]))
    sols.append((values[i][1]))
    
t_norm = time / (np.linalg.norm(time))
y_norm = sols / (np.linalg.norm(sols))

print('done')