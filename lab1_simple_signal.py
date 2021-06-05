import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq


# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Number of sample points for x[n] signal
N = 16
Fs = 16 # sampling frequency
Ts = 1.0 / Fs # time step, is sampling period
#t = np.linspace(0.0, N * T, N, endpoint=False)
# discrete time axis
n = np.arange(0.0, N*Ts, Ts)

# discrete time signal
f1 = 1.0
f2 = 3.0
x_n = 2 * np.sin(2.0 * np.pi * f1 * n) + np.sin(2.0 * np.pi * f2 * n)

# fft
X_k = fft(x_n)

# create frequency axis
k = fftfreq(N, Ts)
idx = np.argsort(k)

# Power spectral density
ps_k = X_k * np.conj(X_k) / N

p_n = x_n**2
print("E_k=",np.sum(ps_k))
print("E_n=",np.sum(p_n))

# plot impulse
plt.stem(k[idx], ps_k[idx], "o")
plt.grid()
plt.show()
