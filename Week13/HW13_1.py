# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 15:13:12 2022

@author: user
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy.fftpack import fft,ifft
import math

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




x1=np.zeros(256,dtype=float)
x2=np.zeros(256,dtype=float)
for i in range(0,256):
    x1[i]=(2/3)**i+(-15/16)**i

for j in range(0,256):
    x2[j]=np.exp(-0.1*j)*(np.sin(np.pi*j/5)+np.cos(0.3*np.pi*j))



plt.figure(0,figsize=(40,15))
plt.subplot(231)
plt.title("x1")
plt.stem(x1)  

plt.subplot(232)
plt.title("x1_DFT")
plt.stem(abs(My_FFT(x1,256)))  

plt.subplot(233)
plt.title("x1_IDFT512")

x3=np.zeros(512,dtype=complex)

for i in range(0,512):
    if(i%2==0):
        x3[i]=My_FFT(x1,256)[int(i/2)]

plt.stem(IFFT(x3,512))  






plt.subplot(234)
plt.title("x2")
plt.stem(x2)  


plt.subplot(235)
plt.title("x2_DFT")
plt.stem(abs(My_FFT(x2,256)))  

plt.subplot(236)
plt.title("x2_IDFT")


x4=np.zeros(512,dtype=complex)

for i in range(0,512):
    if(i%2==0):
        x4[i]=My_FFT(x2,256)[int(i/2)]



plt.stem(IFFT(x4,512))  


