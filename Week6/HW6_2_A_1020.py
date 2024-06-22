# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 14:57:14 2022

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 16:32:04 2022

@author: user
"""

import numpy as np
from matplotlib import pyplot as plt

y=np.zeros(200)

p=np.zeros(200)
for i in range(0,200):
    y[i]=1+np.cos(i*2*np.pi/50)
    
    h=0.5+np.exp(-1j*i*2*np.pi/50)+0.5*np.exp(-2j*i*2*np.pi/50)
    a=np.angle(h)
    p[i]=a
    
    
    
A1=np.zeros(200)
for i in range(0,200,1):
    A1[i]=i*np.pi/25

plt.suptitle("LAB6_2A")
    
plt.subplot(321)
plt.axis([0,2*np.pi, -1 ,2])
plt.stem(A1,y)

plt.subplot(322)
plt.axis([0,2*np.pi, -4 ,4])
plt.stem(A1,p)


plt.subplot(323)
plt.axis([0,8*np.pi, -1 ,2])
plt.stem(A1,y)


plt.subplot(324)
plt.axis([0,8*np.pi, -4 ,4])
plt.stem(A1,p)





y=np.zeros(200)

p=np.zeros(200)
for i in range(0,200):
    y[i]=1+np.cos(i*2*np.pi/50-4*np.pi)


    h=0.5+np.exp(-1j*(i*2*np.pi/50-4*np.pi))+0.5*np.exp(-2j*(i*2*np.pi/50-4*np.pi))
    a=np.angle(h)
    p[i]=a
    
    
    
    
A1=np.zeros(200)
for i in range(0,200,1):
    A1[i]=i*np.pi/25-4*np.pi

plt.subplot(325)

plt.axis([-4*np.pi,4*np.pi, -1 ,2])
plt.stem(A1,y)


plt.subplot(326)

plt.axis([-4*np.pi,4*np.pi, -4 ,4])
plt.stem(A1,p)
