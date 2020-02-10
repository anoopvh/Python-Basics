#!/usr/bin/env python
# coding: utf-8

# # Assignment no :01

# ### Question No: 01 Multiply 2 matrices

# In[2]:


import numpy as np #importing numpy

X = np.array([[1, 4, 3],[3, 5, 6],[6, 7, 9]]) #initializing X and Y
Y = np.array([[1, 2, 5, 12],[6, 7, 3, 0],[4, 7, 9, 11]])

#printing X and Y and their shape

print(X,"\n shape of X : ", X.shape,"\n")
print(Y,"\n shape of Y : ",Y.shape)

Z=np.dot(X,Y) #Matrix Multiplication 
print(Z,"\n shape of Z : ",Z.shape)


# ### Question No: 02 -  Extract all numbers divisible by 3 from the array

# In[100]:


arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12]) #input array
#print(arr) #printing array
arr[(arr >0) & (arr%3==0)] #Selecting the array elements which satisfies the two conditions 
#print(arr[(arr >0) & (arr%3==0)]) 


# ### Question No: 03 -  Get the unique common items between a and b

# In[109]:


a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8]) #initialize the two arrays

np.intersect1d(a,b) #finding the unique values of a and b


# ### Question No: 04 -How to remove from one array those items that exist in another?
# 
# From array a remove all items present in array b

# In[131]:


a = np.array([1,2,3,4,5,11,22,33,44,55])
b = np.array([5,6,7,8,9,10,11])
#print(a,b)

np.setdiff1d(a,b) 

#setdiff1d - Find the set difference of two arrays. 
#Return the sorted, unique values in ar1 that are not in ar2.


# ### Question No: 05. How to get the positions where elements of two arrays match?
# 
# Get the positions where elements of a and b match

# In[133]:


a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

print(a,b)

np.where(a == b)


# ### Question No: 06. How to create a 2D array containing random floats between 10 and 25?
# 
# Create a 2D array of shape 5x3 to contain random decimal numbers between 10 and 25.

# In[40]:


#a=np.random.ranf((10,25))
a=np.zeros(3*5) # creating a 1D array of 3*5 elemets 0

for i in range(15):                  #Begin a for loop i in the range of 0-14
    a[i]=np.random.uniform(10,25)    #generating a random number between 10 - 25
    
a=np.reshape(a,(5,3)) #reshaping the array to the required form and printing
print("2D array of shape 5x3 to contain random float numbers between 10 and 25 \n",a,"\n")


# ### Question No: 07 - Take a string as input. Create a new string that is the reverse of the first string.
# 

# In[49]:


A ="Hello" # initializing the Identifier A as Hello

A[::-1]


# ### Question No: 08 A -  Write a Python program to remove the first occurrence of a specified element  from an array.
# 

# In[4]:


a = np.array([5,6,7,8,7,9,10,11,7,8,9,7,11])  #array Created
i=np.where(a==7) #finding the index of 7 in the arrray
i=i[0]                       #reassign i and choose 0 th element
#print(i,i[0])
np.delete(a,i[0])


# ### Question No: 08 B -  Write a Python program to remove the all occurrence of a specified element  from an array.

# In[5]:


a = np.array([5,6,7,8,7,9,10,11,7,8,9,7,11]) #initializeed the array a
print(a[(a!=7)])                #printing the elements which statisfies the given condition 


# ### Question No: 09. Write a Python program that iterate over elements repeating each as many times as its count.

# In[133]:


a=np.array([2,4,5,8]) #initializeed the array a

for i in a:         # Accessing individual elements from array a
    j=str(i)*i         #creating a copy of int values to str in the array j
    print(j)


# ### Question No: 10 A - Write a Python program to find the occurrences of 10 most common words in a given text.

# In[18]:


a_t="is hello he is hello good bad ab ac"

a=list(a_t)
print(a,type(a),shape(a))


# ### Question No: 10 B - Write a Python program to find the occurrences of 10 most common words which are at least 4 characters long in a given text.

# In[ ]:





# ### Question No: 11 - Create a python program to generate the Fibonocci series.

# In[ ]:




