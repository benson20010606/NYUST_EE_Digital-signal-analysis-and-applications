# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 15:13:12 2022

@author: user
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy.fftpack import fft,ifft
import math
from scipy.io import wavfile

def bit_reverse(x,n):
    result=0
    for i in range (0,n):
        if (x>>i)&1:
            result=result | (1<<(n-i-1))
    return result

def My_FFT(xk,N):
    M=len(xk)
    m1=int(math.log2(M)) #層數
    n=np.arange(1,m1+1)
    w=np.exp(-1j*2*np.pi/2**n)
    x1=np.array(np.zeros(M),dtype="complex")
    #位元反轉
    for index in range(M):
        n1=bit_reverse(index, int(math.log2(M)))
        x1[n1]=xk[index]
    x=x1
    for layer in range(1,m1+1):
        for k in range(1,int(M/pow(2,layer))+1):
            for m in range(1,pow(2,layer-1)+1):
                p=x[(k-1)*pow(2,layer)+m-1]
                q=x[(k-1)*pow(2,layer)+m+pow(2,layer-1)-1]
                x[(k-1)*pow(2,layer)+m-1]=p+q*pow(w[layer-1],m-1)
                x[(k-1)*pow(2,layer)+m+pow(2,layer-1)-1]=p-q*pow(w[layer-1],m-1)
    return x
def My_IFFT(xk,N):
    M=len(xk)
    m1=int(math.log2(M)) #層數
    n=np.arange(1,m1+1)
    w=np.exp(1j*2*np.pi/2**n)
    x1=np.array(np.zeros(M),dtype="complex")
    #位元反轉
    for index in range(M):
        n1=bit_reverse(index, int(math.log2(M)))
        x1[n1]=xk[index]
    x=x1
    
    
    for layer in range(1,m1+1):
        for k in range(1,int(M/pow(2,layer))+1):
            for m in range(1,pow(2,layer-1)+1):
                p=x[(k-1)*pow(2,layer)+m-1]
                q=x[(k-1)*pow(2,layer)+m+pow(2,layer-1)-1]
                x[(k-1)*pow(2,layer)+m-1]=p+q*pow(w[layer-1],m-1)
                x[(k-1)*pow(2,layer)+m+pow(2,layer-1)-1]=p-q*pow(w[layer-1],m-1)
    return x/len(xk)


def IFFT(Xk,N):
    return np.conjugate(My_FFT(np.conjugate(Xk),N))/N




filename='Queen.wav'
freq, audio=wavfile.read(filename)
lens=len(audio)

N=int(lens/1024)


X1=np.arange(0,1024,dtype=complex)


for i in range(0,1024):
    X1[i]=audio[i]


plt.figure(1)

plt.title("Origin")
plt.plot(audio)  



X1RW=fft(X1)
plt.figure(2)
plt.title("Dir_1024")
plt.plot(abs(X1RW))  

################
X2=np.arange(0,1024,dtype=complex)
X3=np.arange(0,1024,dtype=complex)

for i in range (0,N):
    for j in range(0,1024):
        X2[j]=audio[j+1024*i]
    A=My_FFT(X2, 1024)
    for k in range(0,1024):
        X3[k]+=A[k]
    
X3=X3/N
plt.figure(3)
plt.title("Averange")
plt.plot(abs(X3))
#####################


All=fft(audio)
plt.figure(4)
plt.title("All")
plt.plot(abs(All))
######################


n1=np.arange(round(-(1024-1)/2),round((1024-1)/2))


W1=0.54+0.46*np.cos(2*np.pi*n1/1024)


HW1=W1*X1

HM=My_FFT(HW1, 1024)
plt.figure(5)
plt.title("HM 1024")
plt.plot(abs(HM))
########################

X4=np.arange(0,1024,dtype=complex)
X5=np.arange(0,1024,dtype=complex)

for i in range (0,N):
    for j in range(0,1024):
        X4[j]=audio[j+1024*i]
    
    A=My_FFT(X4*W1, 1024)
    for k in range(0,1024):
        X5[k]+=A[k]
X5=X5/N

plt.figure(6)
plt.title("HM_Averange")
plt.plot(abs(X5))