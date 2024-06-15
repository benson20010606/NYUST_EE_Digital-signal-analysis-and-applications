# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 20:23:57 2023

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
Wp=0.6
Ws=0.4
Rp=0.5  
As=60


N1,Wc1 = signal.buttord(Wp,Ws,Rp,As)

b, a = butter(N1, Wc1, 'high', analog=True)
w, h = signal.freqs(b, a)
plt.figure(1)
plt.plot(w, 20 * np.log10(abs(h)))
plt.axis([0,1,-100,0])
plt.title("Buttworth")
#A_Chebyshev
b, a =cheby1(N1, Rp,Wc1, 'high', analog=True)
w, h = signal.freqs(b, a)
plt.figure(2)
plt.plot(w, 20 * np.log10(abs(h)))
plt.axis([0,1,-205,0])
plt.title("Chebyshev")
#A_Elliptic
b, a =ellip(N1, Rp,As,Wc1, 'high', analog=True, output='ba')
w, h = signal.freqs(b, a)
plt.figure(3)
plt.plot(w, 20 * np.log10(abs(h)))
plt.axis([0,1,-100,0])
plt.title("Elliptic")
