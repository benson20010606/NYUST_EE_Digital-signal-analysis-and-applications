# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 17:02:23 2022

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 15:33:49 2022

@author: user
"""
from scipy.io import wavfile
import numpy as np
from matplotlib import pyplot as plt

def DTft(x1,N,num):
    w1=np.zeros(num+1,dtype=complex)
    for n in range(0,num+1):
        w1[n]=0
        for i in range(0,len(x1)):
            w1[n]=w1[n]+x1[i]*np.exp(-1j*np.pi*2/N*i*n)
    return abs(w1)

###################################

####################################


pi=np.pi


filename="thwap3.wav"
freq, audio=wavfile.read(filename)
lens=len(audio)


N=5664

show=np.arange(0,N)
X=DTft(audio,N-1,N-1)

plt.figure(2)
X[0]=0
X[5663]=0
plt.stem(show,X)    


