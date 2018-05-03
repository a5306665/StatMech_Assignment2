
# coding: utf-8

# In[27]:


#有N個同面骰子  可以視為 同一個骰子丟N次 , 故用 上一次作業1修改之 在這裡  times2 為   實驗次數  , times1 為  骰子個數
import time
import random
import numpy as metrix

def dice_twentyface(times2):
    t1 = time.clock()
    
    times1 =2   #多少骰子
    x = 0
    y = 0
    a = 0
    b = 0
    s = 0
    z = 0
    smatrix = s-1
    print("10面骰子")
    print("投擲次數->骰子個數",times1)

    sides = 10  #骰子幾面
    #總共可能性
    histogram = metrix.zeros(sides)
    s1 = metrix.zeros(sides*times1)
    print("1~10次數集合") 
    for i in range(times2):
        r = 0
        s = 0
        for j in range(times1):
            r = int(metrix.random.random()*sides)
            histogram[r] = histogram[r] + 1
            s = s+r+1
        #    print(histogram)
        #    print(s)
        smatrix = s-1
        s1[smatrix] = s1[smatrix] + 1
       # print("1~總和max地個數")
       # print(s1)
    print("1~總和max出線的機率")
    print(s1/times2)
    print("所有號碼各別出現次數")
    print(histogram)
    
    for j in range(times1*sides):
        a =(j+1)*s1[j] + a
        x =x+ (j+1) * s1[j]/times2
        t2=time.clock()
    print("期望值",x)
    for j in range(sides):
        y= y+((j+1-x)**2) * s1[j]/times2
        z=y**0.5
    print("variance",y)
    print("standard",z)
def run():
    dice_twentyface(1)
    dice_twentyface(10)
    dice_twentyface(100)
    dice_twentyface(1000)
    dice_twentyface(10000)

    
run()

