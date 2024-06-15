# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 15:12:15 2022

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
            




X1=np.ones(6,dtype=float)
Y1=DFT_Loop(X1,6)
plt.figure(0,figsize=(12,8))
plt.subplot(241)
plt.title("DFT,N=6")
plt.stem(abs(Y1))  


X1=np.ones(8,dtype=float)
X2=A(X1,8)
Y2=DFT_Loop(X2,8)

plt.subplot(242)
plt.title("DFT,N=8")
plt.stem(abs(Y2)) 



X1=np.ones(16,dtype=float)
X3=A(X1,16)
Y3=DFT_Loop(X3,16)

plt.subplot(245)
plt.title("DFT,N=16")
plt.stem(abs(Y3)) 


X1=np.ones(32,dtype=float)
X4=A(X1,32)
Y4=DFT_Loop(X4,32)

plt.subplot(246)
plt.title("DFT,N=32")
plt.stem(abs(Y4)) 



IY1=IDFT_Loop(Y1,64)
plt.subplot(243)
plt.title("IDFT,N=6")
plt.stem(abs(IY1)) 


IY2=IDFT_Loop(Y2,64)
plt.subplot(244)
plt.title("IDFT,N=8")
plt.stem(abs(IY2)) 

IY3=IDFT_Loop(Y3,64)
plt.subplot(247)
plt.title("IDFT,N=16")
plt.stem(abs(IY3)) 


IY4=IDFT_Loop(Y4,64)
plt.subplot(248)
plt.title("IDFT,N=32")
plt.stem(abs(IY4)) 


'''
A=np.arange(0,10)
B=np.reshape(A,(len(A),1))
C=np.reshape(A,(1,len(A)))
D=np.dot(B,C)  
'''