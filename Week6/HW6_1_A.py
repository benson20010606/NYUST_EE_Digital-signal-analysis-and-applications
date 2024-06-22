# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 15:18:03 2022

@author: user
"""

import numpy as np
from matplotlib import pyplot as plt

y=np.zeros(200)

p=np.zeros(200)
for i in range(0,200):
    y[i]=1/(1+0.64-1.6*np.cos(i*2*np.pi/50))**0.5
    p[i]=-np.arctan(0.8*np.sin(i*2*np.pi/50)/(1-0.8*np.cos(i*2*np.pi/50)))
A1=np.zeros(200)
for i in range(0,200,1):
    A1[i]=i*np.pi/25

plt.suptitle("LAB6_1A")


plt.subplot(321)
plt.axis([0,2*np.pi, -1 ,5])
plt.stem(A1,y)

plt.subplot(322)
plt.axis([0,2*np.pi, -1 ,1])
plt.stem(A1,p)


plt.subplot(323)
plt.axis([0,8*np.pi, -1 ,5])
plt.stem(A1,y)


plt.subplot(324)
plt.axis([0,8*np.pi, -1 ,1])
plt.stem(A1,p)





y=np.zeros(200)

p=np.zeros(200)
for i in range(0,200):
    y[i]=1/(1+0.64-1.6*np.cos(i*2*np.pi/50-4*np.pi))**0.5
    p[i]=-np.arctan(0.8*np.sin(i*2*np.pi/50-4*np.pi)/(1-0.8*np.cos(i*2*np.pi/50-4*np.pi)))
A1=np.zeros(200)
for i in range(0,200,1):
    A1[i]=i*np.pi/25-4*np.pi

plt.subplot(325)

plt.axis([-4*np.pi,4*np.pi, -1 ,5])
plt.stem(A1,y)


plt.subplot(326)

plt.axis([-4*np.pi,4*np.pi, -1 ,1])
plt.stem(A1,p)







