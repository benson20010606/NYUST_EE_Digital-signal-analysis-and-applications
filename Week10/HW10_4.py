# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 17:20:29 2022

@author: user
"""


import numpy as np
from matplotlib import pyplot as plt

p=np.pi
j=0+1j
e=np.exp

def DFT_Loop(x1,n):
    M1=np.zeros((n,n),dtype=complex)
    for i in range(0,n):
        for k in range(0,n):
            M1[i][k]=e((-j*2*p*i*k)/n)
    Xk=M1@x1
    return Xk


def DFT_Matrix(x1,n):
    M0=np.arange(0,n)
    M1=e(-j*2*np.dot(np.reshape(M0,(len(M0),1)),np.reshape(M0,(1,len(M0))))/n)
    Xk=(M1@x1.T).T
    return Xk

def IDFT_Loop(xk,n):
    Xn=np.zeros((n,),dtype=complex)
    for i in range(0,n):
        for k in range(0,len(xk)):
            Xn[i]=Xn[i]+xk[k]*e(j*2*p*i*k/len(xk))
    Xn=Xn/len(xk)        
    return Xn


def IDET_Matrix(xk,n):
    n=np.arange(0,n)
    k=np.arange(0,len(xk))
    A=e(j*2*p*np.dot(np.reshape(n,(len(n),1)),np.reshape(k,(1,len(k))))/len(xk))
    Xn=((A@xk.T)/len(xk)).T
    return Xn



def Cirshift(x,M,N):##在時域進行 環狀位移
    X=np.zeros(N,dtype=float)
    if M>N:
        M=M%N
    for i in range (0,32):
        if(i+M<32):
            X[i+M]=x[i]
        else :
            for a in range(0,M):
                X[a]=x[N-M+a]
    return X

def Cirshift_freq_domain(x,M,N):## 轉到頻域進行 環狀位移
    X=np.zeros(N,dtype=float)
    X=DFT_Loop(x,N)
    for i in range (0,len(X)):
        X[i]=X[i]*e(-j*2*p*i*M/N)
    X=IDFT_Loop(X,N)
    return X

X1=np.zeros(32,dtype=float)
for i in range (0,32):
    X1[i]=5*0.6**i
   
plt.figure(0,figsize=(10,15))
plt.subplot(411)
plt.title("O")
plt.stem(abs(X1))  


Y1=Cirshift_freq_domain(X1,7,32)
plt.subplot(412)
plt.title("M=7")
plt.stem(abs(Y1))


Y2=Cirshift(X1,16,32)
plt.subplot(413)
plt.title("M=16")
plt.stem(abs(Y2))


Y3=Cirshift(X1,40,32)

plt.subplot(414)
plt.title("M=40")
plt.stem(abs(Y3))










