#!/usr/bin/env python
# coding: utf-8

# In[8]:


#cant complete the whole code
#the code is only till the input part
#whether the entry for the column is valid or not
import numpy as np
rows = int(input("rows?"))
if (rows <= 0):
    print("No of rows should be a Natural number. Please try again")
    rows = input("rows?")

cols = int(input("columns?"))

if (cols <= 0):
    print("No of columns should be a Natural number. Please try again")
    cols = input("cols?")
    
pieces = int(input("pieces?"))
if (pieces <= 0):
    print("No of pieces should be a Natural number. Please try again")
    pieces = input("pieces?")
    
grid = np.zeros((rows,cols))
print(grid)

    

def validornot(rows,cols,grid,colum):
    return grid[rows-1][colum] == 0

def nextavail(rows,grid,colum):
    for i in range(rows):
        if (grid[i][colum] == 0):
            return i
    
    pass
    

temp = 0
gameon = True
while gameon:
    if temp == 0:
        colum = int(input("Player 1, what row would you like to place your piece?"))
        if(colum <= 0 or colum >= cols):
             print("No of columns should be between 1 & number of columns. Please try again")
                
        
            
    else:
        colum = int(input("Player 2, what row would you like to place your piece?"))
        if(colum <= 0 or colum >= cols):
             print("No of columns should be between 1 & number of columns. Please try again")
                  
       
    temp += 1
    temp = temp % 2


# ### 

# In[ ]:




