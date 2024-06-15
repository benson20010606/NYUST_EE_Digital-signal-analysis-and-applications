# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 17:24:26 2022

@author: user
"""

import numpy as np
from matplotlib import pyplot as plt
x1=np.zeros(21)
y1=np.zeros(21)
s1=np.zeros(21)
t1=np.zeros(21)

rxy=np.zeros(41)

rxs=np.zeros(41)
#######################
wx5=np.zeros(21)
wy5=np.zeros(21)
wx1=np.zeros(21)
wy1=np.zeros(21)
wx2=np.zeros(21)
wy2=np.zeros(21)
######################
wxx5=np.zeros(41)
wyy5=np.zeros(41)
wxx1=np.zeros(41)
wyy1=np.zeros(41)
wxx2=np.zeros(41)
wyy2=np.zeros(41)
#########################
range_1=np.zeros(41)
range_2=np.zeros(41)

range_A=np.zeros(21)

for i in range(0,5):
    s1[i]=1
for i in range(0,5):
    t1[i]=0.6**i

for i in range(10,15):
    x1[i]=1
for i in range(10,15):
    y1[i]=0.6**(i-10)



for m in range(-20,21):
    c=0
    for k in range(-20,21):
        b=0
        if(k<0):
            a=0
        else:
            a=x1[k]
        if((k-m<0) ):
            b=0
        elif(k-m<21):
            b=y1[k-m]
        c=c+a*b
    rxy[m+20]=c
    range_1[m+20]=m
    
plt.figure(1)
plt.title("rxy")
plt.stem(range_1,rxy)








for m in range(-20,21):
    c=0
    for k in range(-20,21):
        b=0
        if(k<0):
            a=0
        else:
            a=x1[k]
        if((k-m<0) ):
            b=0
        elif(k-m<21):
            b=s1[k-m]
        c=c+a*b
    rxs[m+20]=c
    range_2[m+20]=m
    
plt.figure(2)
plt.title("rxs")
plt.stem(range_2,rxs)
    
##########################b小題

    
wx5=0.5*np.random.randn(21)+x1
wx1=1*np.random.randn(21)+x1
wx2=2*np.random.randn(21)+x1


wy5=0.5*np.random.randn(21)+y1
wy1=1*np.random.randn(21)+y1
wy2=2*np.random.randn(21)+y1


for m in range(-20,21):
    c=0
    for k in range(-20,21):
        b=0
        if(k<0):
            a=0
        else:
            a=x1[k]
        if((k+m<0) ):
            b=0
        elif(k+m<21):
            b=wx5[k+m]
        c=c+a*b
    wxx5[m+20]=c
    range_2[m+20]=m
plt.figure(3)
plt.subplot(311)
plt.title("wxx0.5")
plt.stem(range_2,wxx5)


for m in range(-20,21):
    c=0
    for k in range(-20,21):
        b=0
        if(k<0):
            a=0
        else:
            a=x1[k]
        if((k+m<0) ):
            b=0
        elif(k+m<21):
            b=wx1[k+m]
        c=c+a*b
    wxx1[m+20]=c
    range_2[m+20]=m
plt.subplot(312)
plt.title("wxx1")
plt.stem(range_2,wxx1)


for m in range(-20,21):
    c=0
    for k in range(-20,21):
        b=0
        if(k<0):
            a=0
        else:
            a=x1[k]
        if((k+m<0) ):
            b=0
        elif(k+m<21):
            b=wx2[k+m]
        c=c+a*b
    wxx2[m+20]=c
    range_2[m+20]=m
plt.subplot(313)
plt.title("wxx2")
plt.stem(range_2,wxx2)

#################

for m in range(-20,21):
    c=0
    for k in range(-20,21):
        b=0
        if(k<0):
            a=0
        else:
            a=y1[k]
        if((k+m<0) ):
            b=0
        elif(k+m<21):
            b=wy5[k+m]
        c=c+a*b
    wyy5[m+20]=c
    range_2[m+20]=m
plt.figure(4)
plt.subplot(311)
plt.title("wyy0.5")
plt.stem(range_2,wyy5)


for m in range(-20,21):
    c=0
    for k in range(-20,21):
        b=0
        if(k<0):
            a=0
        else:
            a=y1[k]
        if((k+m<0) ):
            b=0
        elif(k+m<21):
            b=wy1[k+m]
        c=c+a*b
    wyy1[m+20]=c
    range_2[m+20]=m
plt.subplot(312)
plt.title("wyy1")
plt.stem(range_2,wyy1)


for m in range(-20,21):
    c=0
    for k in range(-20,21):
        b=0
        if(k<0):
            a=0
        else:
            a=y1[k]
        if((k+m<0) ):
            b=0
        elif(k+m<21):
            b=wy2[k+m]
        c=c+a*b
    wyy2[m+20]=c
    range_2[m+20]=m
plt.subplot(313)
plt.title("wyy2")
plt.stem(range_2,wyy2)

########驗證
plt.figure(5)
plt.subplot(311)
plt.stem(range_2,np.correlate(wx5,x1,mode="full"))
plt.subplot(312)
plt.stem(range_2,np.correlate(wx1,x1,mode="full"))
plt.subplot(313)
plt.stem(range_2,np.correlate(wx2,x1,mode="full"))


plt.figure(6)
plt.subplot(311)
plt.stem(range_2,np.correlate(wy5,y1,mode="full"))
plt.subplot(312)
plt.stem(range_2,np.correlate(wy1,y1,mode="full"))
plt.subplot(313)
plt.stem(range_2,np.correlate(wy2,y1,mode="full"))












