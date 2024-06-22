# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 16:02:12 2022

@author: user
"""

import numpy as np
from matplotlib import pyplot as plt
x1=np.zeros(160)

y1=np.zeros(160)

for i in range (0,160,1):
    if i-1<0:
        b=0
    else:
        b=y1[i-1]
    y1[i]=0.8*y1[i-1]+np.cos(0.05*i*np.pi)
    x1[i]=i

    
plt.suptitle("LAB6_1C")  
plt.subplot(211)    

plt.stem(x1,y1)


x2=np.zeros(32)

y2=np.zeros(32)

for i in range (0,32,1):
    if i-1<0:
        a=0
    else:
        a=y2[i-1]
    y2[i]=0.8*a+np.cos(0.25*i*np.pi)
    x2[i]=i

    
    
plt.subplot(212)    

plt.stem(x2,y2)






