# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 17:11:47 2022

@author: user
"""

import numpy as np
from matplotlib import pyplot as plt



x1=np.zeros(32)

y1=np.zeros(32)

for i in range (0,32,1):

    y1[i]=5*np.cos(0.25*i*np.pi)
    x1[i]=i

    
    
plt.subplot(211)    

plt.stem(x1,y1)

########################
x2=np.zeros(11)

y2=np.zeros(11)

for i in range (0,11,1):

    y2[i]=np.cos(0.75*i*np.pi)
    x2[i]=i

    
    
plt.subplot(212)    

plt.stem(x2,y2)