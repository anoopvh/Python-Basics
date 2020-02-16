#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

def fibo(n): 
    a=0
    b=1
    fib=np.array([a,b])
    if(n<0): 
        print("Incorrect input") 
    elif (n==0): 
        return a 
    elif (n==1): 
        return b 
    else: 
        for i in range(2,n): 
            c=a+b
            #print(c)
            a=b 
            b=c 
            fib=np.append(fib,c)
        return fib 

while True:
    n,m=map(int,input("Enter the N and M of the NxM matrix : \n").split())
    if (not(n>=3 and (0<m<=7))):
        continue
    else:
        matA=np.zeros((n,m))
        
        for i in range(m):
            i+=1
            matA[0,i-1:i]=i+(i-1)
        for i in range(1,n):
            matA[i:,:]=fibo(m)
        print(matA)
        break

