# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 17:17:17 2022

@author: user
"""

import numpy as np
from matplotlib import pyplot as plt
x1=np.zeros(32)

y1=np.zeros(32)

k1=np.zeros(32)

for i in range (0,32,1):

    k1[i]=5*np.cos(0.25*i*np.pi)



for i in range (0,32,1):
    if i-2<0:
        a2=0
    else:
       a2=k1[i-2]
    if i-1<0:
        a1=0
    else:
       a1=k1[i-1]    
    y1[i]=0.5*k1[i]+a1+0.5*a2
    x1[i]=i

plt.suptitle("LAB6_2C") 
    
plt.subplot(211)    

plt.stem(x1,y1)






x2=np.zeros(11)

y2=np.zeros(11)


k2=np.zeros(11)

for i in range (0,11,1):

    k2[i]=5*np.cos(0.75*i*np.pi)


for i in range (0,11,1):
    if i-2<0:
        b2=0
    else:
       b2=k2[i-2]
    if i-1<0:
        b1=0
    else:
       b1=k2[i-1]    
    y2[i]=0.5*k2[i]+b1+0.5*b2
    x2[i]=i
    
    
plt.subplot(212)    

plt.stem(x2,y2)