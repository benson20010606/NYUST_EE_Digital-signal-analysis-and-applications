# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 13:25:36 2022

@author: user
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy.fftpack import fft,ifft
import math
from scipy import integrate

p=np.pi
j=0+1j
e=np.exp
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



n=np.arange(0,30/4000+1/40000,1/40000 )

signal=5*np.sin(2*np.pi*4000*n)
ns1=signal+(1/3)*np.random.randn(len(signal))
ns2=signal+(2/3)*np.random.randn(len(signal))
ns3=signal+(4/3)*np.random.randn(len(signal))




#Hamming
HN=int(3.3/0.5*40)+1

n1=np.arange(round(-(HN-1)/2),133)


n2=0.17285*2*np.sin(n1*0.17285*2*np.pi)/(0.17285*2*np.pi*n1)
n2[132]=0.17285*2

Hm=0.54+0.46*np.cos(2*np.pi*n1/264)


F1=np.multiply(Hm,n2)


plt.figure(1)

plt.title("F1")
plt.stem(F1)  

plt.figure(2)

plt.title("FFT_F1")


F11=np.append(F1, np.zeros(8192-265))
F1_1=My_FFT(F11,8192)
plt.plot(20*np.log10(abs(F1_1[0:4096]) ))


F1_300=np.append(F1, np.zeros(300-len(F1)))

FFT_F1300=fft(F1_300)


##########################

plt.figure(3,figsize=(8,8))



plt.subplot(321)
plt.plot(abs(fft(ns1)[0:150])) 
plt.subplot(323)
plt.plot(abs(fft(ns2)[0:150]) )
plt.subplot(325)
plt.plot(abs(fft(ns3)[0:150]) )

plt.subplot(322)
plt.plot(abs(fft(ns1)[0:150]*FFT_F1300[0:150])) 
plt.subplot(324)
plt.plot(abs(fft(ns2)[0:150]*FFT_F1300[0:150]) )
plt.subplot(326)
plt.plot(abs(fft(ns3)[0:150]*FFT_F1300[0:150]) )
