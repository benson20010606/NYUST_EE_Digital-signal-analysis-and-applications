# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 12:07:23 2022

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
def DFT_Matrix(x1,n):
    M0=np.arange(0,n)
    M1=e(-j*2*np.dot(np.reshape(M0,(len(M0),1)),np.reshape(M0,(1,len(M0))))/n)
    Xk=(M1@x1.T).T
    return Xk


def i(x):
    n1=np.arange(round(-(87-1)/2),43+1)
    return np.exp(6.76*np.roots(1-(2*n1/86)**2)*np.cos(x))

def ib(sita):
    
    return  np.exp(6.76*np.cos(sita))

fs=0.4/2
fp=0.6/2

fp1=fs+(fp-fs)/2

N=int(5.5/((fp-fs)))#55


n1=np.arange(round(-(55-1)/2),27+1)
n2=np.arange(0,55)
F2=-2*fp1*np.sin(n1*fp1*2*np.pi)/(fp1*2*np.pi*n1)
F2[27]=1-fp1*2

BM=0.42-0.5*np.cos(2*np.pi*n2/54)+0.08*np.cos(4*np.pi*n2/54)

H2=np.multiply(BM,F2)

plt.figure(1,figsize=(8,7))

plt.subplot(211)
plt.title("BM")
plt.stem(H2) 

plt.subplot(212)

plt.title("FFT_BM")

F2=np.append(H2, np.zeros(8192-55))
F2_1=My_FFT(F2,8192)
plt.plot(20*np.log10(abs(F2_1[0:4096]) )) 

