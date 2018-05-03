
# coding: utf-8

# In[38]:


import time
import random
import numpy as metrix

def dice_twentyface(times):
    t1 = time.clock()
    x = 0
    y = 0
    s = 0
    a=0
    
    sides1 = 6
    sides2 = 4
    histogram = metrix.zeros(sides1)
    h2 = metrix.zeros(sides2)
    s1 = metrix.zeros(sides1+sides2)
    r1 = 0
    r2 = 0
    for i in range(times):
        r1 = int(metrix.random.random()*sides1)
        r2 = int(metrix.random.random()*sides2)
        histogram[r1] = histogram[r1] + 1
        h2[r2] = h2[r2]+1
        s = r1+1 + r2
        s1[s] = s1[s] + 1 
    print(histogram)
    print(h2)
    print("總和1~max的次數")
    print(s1)
    print("總和1~max個別的機率")
    print(s1/times)    

def run():
    dice_twentyface(1)
    dice_twentyface(10)
    dice_twentyface(100)
    dice_twentyface(1000)
    dice_twentyface(10000)
    dice_twentyface(100000)
    dice_twentyface(1000000)
    
run()


