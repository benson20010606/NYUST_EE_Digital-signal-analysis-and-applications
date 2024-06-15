# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 16:27:15 2022

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

def A(x1,n):
    for i in range(0,n):
        if(i>=6):
            x1[i]=0
    return x1
            

X1=np.ones(45,dtype=float)
for i in range(0,45):
    X1[i]=0.95**i


Y1=DFT_Loop(X1,45)
plt.figure(0,figsize=(10,7))
plt.subplot(231)
plt.title("DFT,N=45")
plt.stem(abs(Y1))  

plt.subplot(234)
plt.title("IDFT,N=45")
plt.stem(abs(IDFT_Loop(Y1,45)))  


X2=np.zeros(100,dtype=float)
for i in range(0,45):
    X2[i]=0.95**i

Y2=DFT_Loop(X2,100)

plt.subplot(232)
plt.title("DFT,N=100")
plt.stem(abs(Y2))  

plt.subplot(235)
plt.title("IDFT,N=45")
plt.stem(abs(IDFT_Loop(Y2,100)))  


Y3=np.zeros(25,dtype=complex)
for i in range(0,100):
    if i%4==0:
        Y3[int(i/4)]=Y2[i]


plt.subplot(233)
plt.title("DFT,N=100,K=25")
plt.stem(abs(Y3)) 

plt.subplot(236)
plt.title("IDFT,N=100,K=25")
plt.stem(abs(IDFT_Loop(Y3,100)))










