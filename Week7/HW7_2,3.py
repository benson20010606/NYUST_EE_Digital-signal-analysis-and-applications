# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 15:33:49 2022

@author: user
"""

import numpy as np
from matplotlib import pyplot as plt

def DTft(x1,N,num):
    w1=np.zeros(num+1,dtype=complex)
    for n in range(0,num+1):
        w1[n]=0
        for i in range(0,len(x1)):
            w1[n]=w1[n]+x1[i]*np.exp(-1j*np.pi*2/N*i*n)
    return abs(w1)

###################################
X=np.zeros(101,dtype=complex)
for i in range (0,101):
    X[i]=(0.9*np.exp(1j*np.pi/3))**i
####################################


    
range_1=np.zeros(1001)    
for i in range (0,1001):
    range_1[i]=i/1000*np.pi*8-4*np.pi


range_2=np.zeros(201)    
for i in range (0,201):
    range_2[i]=i/200*np.pi*8-4*np.pi
    
plt.figure(0)
plt.title("1000")
plt.stem(range_1,DTft(X,250,1000))  
    
    
plt.figure(1)
plt.title("200")

plt.stem(range_2,DTft(X,50,200))    
