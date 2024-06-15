# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 15:15:09 2022

@author: user
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy.fftpack import fft,ifft
import math


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


n1=np.arange(round(-(53-1)/2),26+1)


n2=0.21875*2*np.sin(n1*0.21875*2*np.pi)/(0.21875*2*np.pi*n1)
n2[26]=0.21875*2

Hm=0.54+0.46*np.cos(2*np.pi*n1/52)

F1=np.multiply(Hm,n2)
plt.figure(1)

plt.title("F1")
plt.stem(F1)  


f2=(0.35+0.275)/2
f1=0.35/4

plt.figure(2)
    
plt.title("FFT_F1")


F1=np.append(F1, np.zeros(8192-53))
F1_1=My_FFT(F1,8192)
plt.plot(20*np.log10(abs(F1_1[0:4096]) ))

#############################################################
        
N2=np.arange(round(-(75-1)/2),38)

BM=0.42+0.5*np.cos(2*np.pi*N2/74)+0.08*np.cos(4*np.pi*N2/74)

H2=2*f2*np.sin(N2*f2*2*np.pi)/(N2*2*f2*np.pi)-2*f1*np.sin(N2*2*f1*np.pi)/(N2*2*f1*np.pi)
H2[37]=2*(f2-f1)

F2=BM*H2

plt.figure(3)

plt.title("F2")
plt.stem(F2) 

plt.figure(4)

plt.title("FFT_F2")

F2=np.append(F2, np.zeros(8192-75))
F2_1=My_FFT(F2,8192)
plt.plot(20*np.log10(abs(F2_1[0:4096]) )) 





