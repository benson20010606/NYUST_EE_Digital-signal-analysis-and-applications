# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 15:15:12 2022

@author: user
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy.fftpack import fft,ifft
import math



#輸入 X、H 長度L 切幾段K

def OAM(X,H,L):
    M=len(H)
    N=L+M-1
    K=int(len(X)/L)
    h=np.append(H, np.zeros(L-1))
    Hk=fft(h,len(h))
    y=np.array([])
    for i in range(0,K):
        x=X[i*L:(i+1)*L]
        Xn=np.append(x, np.zeros(M-1))
        Xk=fft(Xn,len(Xn))

        Yk=np.multiply(Xk,Hk)
        
        yn=ifft(Yk,N)
        if(i==0):
            y=yn
        else:
            for j in range(0,M-1):
                y[j+i*L]=y[j+i*L]+yn[j]
                
            y=np.append(y[0:i*L+N],yn[M-1:N])

        
    return y[0:len(X)]


def OSM(X,H,L):
    M=len(H)
    N=L+M-1
    K=int(len(X)/L)
    h=np.append(H, np.zeros(L-1))
    Hk=fft(h,len(h))
    x1=np.append(np.zeros(M-1), X)
    y=np.array([])
    for i in range(0,K):
        x=x1[i*L:N+i*L]
        ##Xn=np.append(x, np.zeros(M-1))
        Xk=fft(x,len(x))
        
        Yk=np.multiply(Xk,Hk)
        
        yn=ifft(Yk,N)
        if(i==0):
            y=yn[M-1:N]
        else:
            y=np.append(y[0:(i+1)*L],yn[M-1:N])

            
    return y[0:len(X)]
##Input
N=np.arange(0,1024)
Xn=np.exp(-0.2*N)*np.sin(np.pi*N/5)
N=np.arange(0,20)
Hn=(2/3)**N+(-1/4)**N
##Input

y=OAM(Xn,Hn,64)
y1=OSM(Xn,Hn,64)

plt.figure(0,figsize=(10,10))

plt.subplot(311)
plt.title("ANS")
Ans=np.convolve(Xn, Hn)
plt.plot(Ans)  

plt.subplot(312)
plt.title("OAM")
plt.plot(y)  

plt.subplot(313)
plt.title("OSM")
plt.plot(y1)  

##end