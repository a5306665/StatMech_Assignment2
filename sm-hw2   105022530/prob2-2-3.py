
# coding: utf-8

# In[39]:


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
    sides3 = 6
    histogram = metrix.zeros(sides1)
    h2 = metrix.zeros(sides2)
    h3 = metrix.zeros(sides3)
    s1 = metrix.zeros(sides1+sides2+sides3)
    r1 = 0
    r2 = 0
    r3 = 0
    for i in range(times):
        r1 = int(metrix.random.random()*sides1)
        r2 = int(metrix.random.random()*sides2)
        r3 = int(metrix.random.random()*sides3)
        histogram[r1] = histogram[r1] + 1
        h2[r2] = h2[r2]+1
        h3[r3] = h3[r3]+1
        s = r1+1 + r2+1 + r3
        s1[s] = s1[s] + 1 
    print("histogram")    
    print(histogram)
    print("h2")
    print(h2)
    print("h3")
    print(h3)
    print("s1")
    print(s1)
    print("機率分布")
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



