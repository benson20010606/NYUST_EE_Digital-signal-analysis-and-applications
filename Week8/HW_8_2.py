# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 16:02:10 2022

@author: user
"""

from scipy.io import wavfile
import numpy as np
from matplotlib import pyplot as plt
from scipy.fftpack import fft
from scipy import signal

filename='thwap3.wav'
freq, audio=wavfile.read(filename)
lens=len(audio)

y=np.zeros(int(lens/2))

for i in range(0,int(lens/2)):
        y[i]=audio[i*2]


z=np.ones(lens)*np.mean(y)
for i in range(0,lens):
    if i%2==0:
        z[i]=y[int(i/2)]
plt.figure(2)
plt.title("0")
plt.plot(z) 


z1=np.zeros(lens,dtype=float)

for i in range(0,lens):
    if i%2==0:
        z1[i]=y[round(i/2)]
for i in range(0,lens-1):
    if i%2==1:
        z1[i]=(z1[i+1]+z1[i-1])/2

        
plt.figure(3)
plt.title("linear")
plt.plot(z1) 
       



dataFFt_1=fft(z)
dataFFtabs_1=abs(dataFFt_1)
plt.figure(4)
plt.plot(dataFFtabs_1[1:lens])


dataFFt_2=fft(z1)
dataFFtabs_2=abs(dataFFt_2)
plt.figure(5)
plt.plot(dataFFtabs_2[1:lens])

