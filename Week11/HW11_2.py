# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 16:47:07 2022

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
    x1=np.array(np.zeros(M),dtype=complex)
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

#####FFT
x1=np.ones(45,dtype=complex)
for i in range(0,45):
    x1[i]=0.95**i
X1=np.append(x1, np.zeros(128-45))
plt.figure(0,figsize=(15,15))
plt.subplot(221)
plt.title("original")
plt.plot(abs(X1))  

X2=fft(X1)

plt.subplot(222)
plt.title("fft")
plt.plot(abs(X2))  


Xa=My_FFT(X1, 128)

plt.subplot(223)
plt.title("MY_fft")
plt.plot(abs(Xa))  
#對原式之FFT 轉IFFT記得查看FFT之型態是否為Complex
X2=np.zeros(32,dtype=complex)
for i in range(0,32):
        X2[int(i)]=Xa[i*4]
Xb=X2

plt.subplot(224)
plt.title("MY_fft_Downsample")
plt.plot(abs(Xb))
#######

######IFFT


##原始圖像 FFT後降取樣 IFFT
plt.figure(1,figsize=(15,15))
plt.subplot(221)
plt.title("MY_iFFT_Downsample")
plt.plot(abs(My_IFFT(Xb, 32)))  



plt.subplot(222)
plt.title("iFFT_Downsample")
plt.plot(abs(ifft(Xb)))  

##原始圖像 FFT後 IFFT
plt.subplot(223)
plt.title("iFFT_128")
plt.plot(abs(ifft(Xa)))  

##原始圖像
plt.subplot(224)
plt.title("original")
plt.plot(abs(X1))  

'''
##原始圖像
plt.figure(2,figsize=(15,15))
plt.subplot(221)
plt.title("original")
plt.plot(abs(X1))  

plt.subplot(222)
plt.title("MY_iFFT_Downsample_zero_pading")
plt.plot(abs(abs(My_IFFT(np.append(Xb, np.zeros(128-32)), 128)))) 

#########end

'''