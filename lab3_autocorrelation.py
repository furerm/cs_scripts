import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq, ifft


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
f1 = 2.0
f2 = 7.0
x_n = np.sin(1.0 * np.pi * f1 * n) + np.sin(1.0 * np.pi * f2 * n)

auto_corr = np.correlate(x_n, x_n, mode="full")[N-1:]

# fft of auto correlation
X_k = fft(auto_corr)

# create frequency axis
k = fftfreq(auto_corr.size, Ts)
idx = np.argsort(k)

# Power spectral density
ps_k = X_k * np.conj(X_k) / N

p_n = x_n**2

fig = plt.figure()
ax1 = fig.add_subplot(211)
ax1.plot(ps_k[:15])
ax1.set_xticks(k[:15]) # setting the ticks
#ax1.set_xlabel('x')
#ax1.set_ylabel('y')
ax1.grid()
ax2 = fig.add_subplot(212)
ax2.plot(x_n)
#ax2.set_xticks(n) # setting the ticks
#ax2.set_xlabel('x')
#ax2.set_ylabel('y')
ax2.grid()

