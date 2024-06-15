# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 15:22:08 2023

@author: user
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy.fftpack import fft,ifft
import math
from scipy.signal import remez,butter,ellip,cheby1,lfilter
from scipy import signal
pi=np.pi
log=np.log10



#A_Buttworth
Wp=1500/4000
Ws=2000/4000
Rp=0.1
As=50
N1,Wc1 = signal.buttord(Wp,Ws,Rp,As)


b, a = butter(N1, Wc1, 'low', analog=True)
w, h = signal.freqs(b, a)

pha = np.angle(h)

plt.figure(1)
plt.subplot(3,1,1)
plt.title("A_Buttworth_DB")
plt.plot(w*4000, 20 * np.log10(abs(h)))
plt.axis([0,0.5*8000,-205,0])






#A_Chebyshev
b, a =cheby1(N1, Rp,Wc1, 'low', analog=True)
w, h = signal.freqs(b, a)
plt.figure(2)
plt.title("A_Chebyshev")
plt.plot(w*4000, 20 * np.log10(abs(h)))
plt.axis([0,0.5*8000,-205,0])

#A_Elliptic
b, a =ellip(N1, Rp,As,Wc1, 'low', analog=True, output='ba')
w, h = signal.freqs(b, a)
plt.figure(3)
plt.title("A_Elliptic")
plt.plot(w*4000, 20 * np.log10(abs(h)))
plt.axis([0,0.5*8000,-100,0])



#=========================B==========================

#B_Buttworth
W1s=0.1
W1p=0.25
W2p=0.55
W2s=0.7
Rp=1
As=60
N,Wc= signal.buttord([W1p, W2p], [W1s, W2s], Rp, As, True)
b, a =butter(N, Wc, 'bandpass', True)
w, h = signal.freqs(b, a)
plt.figure(4)
plt.title("B_Buttworth")
plt.plot(w*4000, 20 * np.log10(abs(h)))
plt.axis([0,0.5*8000,-80,0])

#B_Chebyshev
N,Wc= signal.cheb1ord([W1p, W2p], [W1s, W2s], Rp, As, True)
b, a = cheby1(N,Rp, Wc, 'bandpass',analog=True,output='ba')
w, h = signal.freqs(b, a)
plt.figure(5)
plt.plot(w*4000, 20 * np.log10(abs(h)))
plt.axis([0,0.5*8000,-80,0])
plt.title("B_Chebyshev")
#B_Elliptic
N,Wc= signal.ellipord([W1p, W2p], [W1s, W2s], Rp, As, True)
b, a = ellip(N,Rp,As, Wc, 'bandpass',analog=True,output='ba')
w, h = signal.freqs(b, a)
plt.figure(6)
plt.plot(w*4000, 20 * np.log10(abs(h)))
plt.axis([0,0.5*8000,-80,0])
plt.title("B_Elliptic")






