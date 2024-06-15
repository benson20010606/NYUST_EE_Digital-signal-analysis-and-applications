# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 13:33:56 2022

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

Y1=np.zeros(41,dtype=complex)

x1=0.8**np.arange(0,41)
h1=np.append(np.ones(17), np.zeros(41-17))

X1=DFT_Loop(x1,41)
H1=DFT_Loop(h1,41)
for i in range (0,41):
    Y1[i]=X1[i]*H1[i]
y1=IDFT_Loop(Y1,41)


plt.figure(0,figsize=(15,15))
plt.subplot(322)
plt.title("(a).Cir,N=41")
plt.stem(abs(y1))  


x2=np.append(x1, np.zeros(50-41))
h2=np.append(h1, np.zeros(50-41))
Y2=np.append(Y1, np.zeros(50-41))

X2=DFT_Loop(x2,50)
H2=DFT_Loop(h2,50)
for i in range (0,50):
    Y2[i]=X2[i]*H2[i]
y2=IDFT_Loop(Y2,50)



plt.subplot(323)
plt.title("(b).Cir,N=50")
plt.stem(abs(y2))


x3=np.append(x2, np.zeros(64-50))
h3=np.append(h2, np.zeros(64-50))
Y3=np.append(Y2, np.zeros(64-50))

X3=DFT_Loop(x3,64)
H3=DFT_Loop(h3,64)
for i in range (0,64):
    Y3[i]=X3[i]*H3[i]
y3=IDFT_Loop(Y3,64)



plt.subplot(326)
plt.title("Cir,N=64")
plt.stem(abs(y3))

y4=np.convolve(x3, h3)


plt.subplot(324)
plt.title("(c).conv,N=64")
plt.stem(abs(y4))



