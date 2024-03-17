#### auto imports modules and classes ####
from benchmarks.plots import plotting_script as plotter
from benchmarks.load_bench_script import load_func
from benchmarks import integrate_greens as greens
import matplotlib.pyplot as plt
import numpy as np

import h5py
import scipy
import pathlib
import pyDOE

#tmp = pyDOE.lhs(2, samples=5000, criterion = 'maximin')
#t1 = tmp[:,0] * 50
#c1 = tmp[:,1] * 0.8 + 0.6

#tmp2 = pyDOE.lhs(3, samples = 5000, criterion = 'maximin')
#t2 = tmp2[:,0] * 50
#c2 = tmp2[:,1] * 0.8 + 0.6
#x0_2 = tmp2[:,2] * 20

tmp3 = pyDOE.lhs(3, samples = 1000, criterion = 'maximin')
t3 = tmp2[:,0] * 50
c3 = tmp2[:,1] * 0.8 + 0.6
sigma = tmp2[:,2] * 20


#for i in range(t1.size):
#    greens.plane_IC(t1[i], c = c1[i], npnts = 250)

#for i in range(t2.size):
#    greens.square_IC(t2[i], npnts = 250, c = c2[i], x0 = x0_2[i])

for i in range(t3.size):
    greens.gaussian_source_IC(t2[i], npnts = 250, c = c2[i], sigma = sigma[i])
