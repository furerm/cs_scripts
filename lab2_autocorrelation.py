import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
import math


# -*- coding: utf-8 -*-
"""
example of:
    create a signal
    autocorrelation of the signal
    plot autocorrelation starting from 0 position
    plot signal with discrete time (indexes)
    plot signal with discrete time (time steps)
"""

# Number of sample points for x[n] signal
N = 128
Fs = 4 # sampling frequency
Ts = 1.0 / Fs # time step, is sampling period
# discrete time axis
n = np.arange(0.0, N*Ts, Ts)

# discrete time signal
f1 = 2.0
f2 = 6.0
x_n = np.sin(2.0 * np.pi * f1 * n) #+ np.sin(2.0 * np.pi * f2 * n)

# calculate autocorrelation and keep results with the size of smaller seq
auto_corr = np.correlate(x_n, x_n, mode='full')[len(x_n)-1:]

fig = plt.figure()
ax1 = fig.add_subplot(311)
ax1.plot(auto_corr)
ax1.set_xticks(np.arange(0, len(auto_corr),1)) # setting the ticks
ax1.set_xlabel('n [samples]')
ax1.set_ylabel('AutoCorrelation')
ax1.grid()
ax2 = fig.add_subplot(312)
ax2.plot(x_n)
ax2.set_xticks(np.arange(0, len(x_n),1)) # setting the ticks
ax2.set_xlabel('n [samples]')
ax2.set_ylabel('Signal')
ax2.grid()
ax3 = fig.add_subplot(313)
ax3.plot(n, x_n)
ax3.set_xlabel('time [sec]')
ax3.set_ylabel('Signal')
ax3.grid()
