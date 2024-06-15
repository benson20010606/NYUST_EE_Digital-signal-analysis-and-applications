# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 15:10:30 2022

@author: user
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy.fftpack import fft,ifft
import math
from scipy.signal import remez

def p(x) :
    return (10**(x/20)-1)/(10**(x/20)+1)

def s(x) :
    return 10**(x/-20)

fs = 8000.0        # Sample rate, Hz
band = [1000, 2200]  # Desired stop band, Hz
trans_width = 600    # Width of transition from pass band to stop band, Hz
numtaps = 31        # Size of the FIR filter.
edges = [0, band[0] - trans_width, band[0], band[1], band[1] + trans_width, 0.5*fs]


plt.figure(0)
plt.subplot(211)
plt.title("bandpass1")
bp1 = remez(31, edges, [0, 1, 0], [1,s(60)/p(1),1],fs=8000)
plt.stem(bp1)


bp1f=np.append(bp1, np.zeros(8192-31))

bp1f=fft(bp1f,8192)

plt.subplot(212)
plt.plot(20*np.log10(abs(bp1f)[0:4096]))

#############################

fs = 15000.0        # Sample rate, Hz
band = [900, 1100]  # Desired stop band, Hz
trans_width =450   # Width of transition from pass band to stop band, Hz
numtaps = 38        # Size of the FIR filter.
edges = [0, band[0] - trans_width, band[0], band[1], band[1] + trans_width, 0.5*fs]


plt.figure(1)
plt.title("bandpass2")
plt.subplot(211)
bp2 = remez(38, edges, [0, 1, 0],  [1,s(30)/p(0.87),1],fs=15000)
plt.stem(bp2)

bp2f=np.append(bp2, np.zeros(15000-38))

bp2f=fft(bp2f,15000)

plt.subplot(212)
plt.plot(20*np.log10(abs(bp2f)[0:7500]))

#############################################

fs = 8000.0        # Sample rate, Hz
band = [1500, 2000]  # Desired stop band, Hz
trans_width =0   # Width of transition from pass band to stop band, Hz
numtaps = 43        # Size of the FIR filter.
edges = [0,1500,2000 ,0.5*fs]


plt.figure(2)

plt.subplot(211)
plt.title("lowpass1")
lp1 = remez(43, edges, [1,0],[s(50)/p(0.1),1], fs=8000)
plt.stem(lp1)

lp1f=np.append(lp1, np.zeros(8192-43))

lp1f=fft(lp1f,8192)

plt.subplot(212)
plt.plot(20*np.log10(abs(lp1f)[0:4096]))

#####################################



fs = 8000.0        # Sample rate, Hz
band = [2000, 2600]  # Desired stop band, Hz
trans_width =0   # Width of transition from pass band to stop band, Hz
numtaps = 29       # Size of the FIR filter.
edges = [0,2000,2600 ,0.5*fs]


plt.figure(3)

plt.subplot(211)
plt.title("highpass1")
hp1 = remez(29, edges,[0,1],[1,s(50)/p(0.5)],fs=8000)
plt.stem(hp1)

hp1f=np.append(hp1, np.zeros(8000-29))

hp1f=fft(hp1f)

plt.subplot(212)
plt.plot(20*np.log10(abs(hp1f)[0:4000]))

