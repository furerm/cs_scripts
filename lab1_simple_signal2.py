import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq


# -*- coding: utf-8 -*-
"""
OK
Spyder Editor
    define the signal using time duration and highest frequency
    
"""
# total time of sampling. In seconds
t_sampling = 2

# Number of sample points for x[n] signal per period
N = 32

# discrete time signal
# highest  frequency 
f1 = 4.0
f2 = 2.0

# period of  highest  frequency 
T1 = 1.0 / f1 

# fix samples per period, time step
Ts = T1 / N

# sampling frequency
Fs = 1 / Ts

# discrete time axis
n = np.arange(0.0, t_sampling, Ts)

# discrete time axis only indexes
nn = np.arange(0.0, len(n), 1)
x_n = np.sin(2.0 * np.pi * f1 * n) #+ np.sin(2.0 * np.pi * f2 * n)

# fft
X_k = fft(x_n)

# create frequency axis
# this values are some thing like: [0..63 -64..-1]
kk = fftfreq(len(n), Ts)
k = kk[:len(n)//2] # only get the positive indexes

# Power spectral density
# Parseval's theorem
ps_k = X_k * np.conj(X_k) / len(n)

p_n = x_n**2

print("Total energy E_k=",np.sum(ps_k.real))
print("Total energy E_n=",np.sum(p_n))
###################################3

fig = plt.figure()
ax11 = fig.add_subplot(221)
ax11.plot(n, x_n)
ax11.grid()

# maybe is the half of the power because of plot only positive freq
ax12 = fig.add_subplot(222)
ax12.plot(k, 2*ps_k[:len(n)//2]) # multiply by 2 to compensate negative freq
ax12.set_xticks(np.arange(0,len(n)//2,1)) # setting the ticks
ax12.grid()

ax21 = fig.add_subplot(223)
ax21.plot(nn, x_n)
ax21.set_xticks(np.arange(0,len(n)-1,5)) # setting the ticks
ax21.grid()
