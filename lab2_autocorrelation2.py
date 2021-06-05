import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
import math


# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Number of sample points for x[n] signal
N = 32
Fs = 16 # sampling frequency
Ts = 1.0 / Fs # time step, is sampling period
# discrete time axis
n = np.arange(0.0, N*Ts, Ts)

# discrete time signal
f1 = 1.0
f2 = 3.0
x_n = 1 * np.sin(2.0 * np.pi * f1 * n) #+ np.sin(2.0 * np.pi * f2 * n)

# calculate autocorrelation and keep results with the size of smaller seq
auto_corr = np.correlate(x_n, x_n, mode='full')
n_corr = np.arange(-(N-1),N,1)

# Total energy
p_n = x_n**2
A = np.abs(np.sum(p_n))
auto_corr_norm = auto_corr / A

fig = plt.figure(figsize=(12, 12))
ax1 = fig.add_subplot(311)
# if I avoid the x-axis the plot start from zero
ax1.plot(n_corr, auto_corr_norm)
ax1.set_xticks(np.arange(-(N-1),N,1)) # setting the ticks
ax1.set_xlabel('n [samples]')
ax1.set_ylabel('AutoCorrelation')
ax1.grid()
# ax2 = fig.add_subplot(312)
# ax2.plot(x_n)
# ax2.set_xticks(np.arange(0, len(x_n),1)) # setting the ticks
# ax2.set_xlabel('n [samples]')
# ax2.set_ylabel('Signal')
# ax2.grid()
# ax3 = fig.add_subplot(313)
# ax3.plot(n, x_n)
# #ax3.set_xticks(np.arange(0, len(x_n),1)) # setting the ticks
# ax3.set_xlabel('time [sec]')
# ax3.set_ylabel('Signal')
# ax3.grid()
