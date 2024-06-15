# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 20:31:13 2023

@author: user
"""


import numpy as np
from matplotlib import pyplot as plt
from scipy.fftpack import fft,ifft
import math
from scipy.signal import remez,butter,ellip,cheby1,lfilter
from scipy import signal

W1p=900/7500
W2p=1100/7500

W1s=(900-450)/7500
W2s=(1100+450)/7500
Rp=0.87
As=30

N1,Wc1= signal.buttord([W1p, W2p], [W1s, W2s], Rp, As, True)
b, a =butter(N1, Wc1, 'bandpass', True)
w, h = signal.freqs(b, a)
plt.figure(1)
plt.plot(w*7500, 20 * np.log10(abs(h)))
plt.axis([0,7500,-40,0])
plt.title("Buttworth")
#Chebyshev
N1,Wc1= signal.cheb1ord([W1p, W2p], [W1s, W2s], Rp, As, True)
b, a = cheby1(N1,Rp, Wc1, 'bandpass',analog=True,output='ba')
w, h = signal.freqs(b, a)
plt.figure(2)
plt.plot(w*7500, 20 * np.log10(abs(h)))
plt.axis([0,7500,-50,0])
plt.title("Chebyshev")
#Elliptic
N1,Wc1= signal.ellipord([W1p, W2p], [W1s, W2s], Rp, As, True)
b, a = ellip(N1,Rp,As, Wc1, 'bandpass',analog=True,output='ba')
w, h = signal.freqs(b, a)
plt.figure(3)
plt.plot(w*7500, 20 * np.log10(abs(h)))
plt.axis([0,7500,-40,0])
plt.title("Elliptic")