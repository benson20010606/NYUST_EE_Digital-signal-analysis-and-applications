# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 15:15:46 2022

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
range_1=np.arange(0,lens)
plt.figure(1)
plt.title("org")
plt.plot(range_1,audio) 

audio_1=np.zeros(int(lens/2))

for i in range(0,int(lens/2)):
        audio_1[i]=audio[i*2]
plt.figure(2)
plt.title("half")
plt.plot(audio_1) 






a=int(lens/2)
audio_2=np.ones(lens)*np.mean(audio)
for i in range(0,lens):
    if i<a:
        audio_2[i]=audio_1[i]

plt.title("zer0")
plt.plot(audio_2)


dataFFt_1=fft(audio)
dataFFtabs_1=abs(dataFFt_1)
plt.figure(4)
plt.plot(dataFFtabs_1[1:lens])


dataFFt_2=fft(audio_2)
dataFFtabs_2=abs(dataFFt_2)
plt.figure(5)
plt.plot(dataFFtabs_2[1:lens])


