# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 14:26:39 2022

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


n=np.arange(0,3/3000+1/300000,1/300000)
signal2=5*np.sin(2*np.pi*4000*n)*np.sin(2*np.pi*50000*n)
ns21=signal2+(1/3)*np.random.randn(len(signal2))
ns22=signal2+(2/3)*np.random.randn(len(signal2))
ns23=signal2+(4/3)*np.random.randn(len(signal2))

f2=0.20166666
f1=0.135

N=101#猜

N2=np.arange(round(-(101-1)/2),51)

BM=0.42+0.5*np.cos(2*np.pi*N2/74)+0.08*np.cos(4*np.pi*N2/74)

H2=2*f2*np.sin(N2*f2*2*np.pi)/(N2*2*f2*np.pi)-2*f1*np.sin(N2*2*f1*np.pi)/(N2*2*f1*np.pi)
H2[50]=2*(f2-f1)

F2=BM*H2


plt.figure(1)

plt.title("F2")
plt.stem(F2)  

plt.figure(2)

plt.title("FFT_F1")

F22=np.append(F2, np.zeros(8192-101))
F2_1=My_FFT(F22,8192)

plt.plot(20*np.log10(abs(F2_1[0:4096]) )) 


F2_300=np.append(F2, np.zeros(300-len(F2)))

FFT_F2300=fft(F2_300)


#####################
plt.figure(3,figsize=(8,8))



plt.subplot(321)
plt.plot(abs(fft(ns21)[0:150])) 
plt.subplot(323)
plt.plot(abs(fft(ns22)[0:150]) )
plt.subplot(325)
plt.plot(abs(fft(ns23)[0:150]) )


plt.subplot(322)
plt.plot(abs(fft(ns21)[0:150]*FFT_F2300[0:150])) 
plt.subplot(324)
plt.plot(abs(fft(ns22)[0:150]*FFT_F2300[0:150]) )
plt.subplot(326)
plt.plot(abs(fft(ns23)[0:150]*FFT_F2300[0:150]) )