#!/usr/bin/env python
# coding: utf-8

# # Basic Python

# ## 1. Split this string

# In[2]:


s = "Hi there Sam!"


# In[3]:


s.split()


# ## 2. Use .format() to print the following string. 
# 
# ### Output should be: The diameter of Earth is 12742 kilometers.

# In[4]:


planet = "Earth"
diameter = 12742


# In[5]:


planet = "Earth"
diameter = 12742
print( 'The diameter of {} is {} kilometers.' .format(planet,diameter));


# ## 3. In this nest dictionary grab the word "hello"

# In[ ]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


# In[6]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(d['k1'][3]["tricky"][3]['target'][3])


# # Numpy

# In[8]:


import numpy as np


# ## 4.1 Create an array of 10 zeros? 
# ## 4.2 Create an array of 10 fives?

# In[11]:


array=np.zeros(10)
print("An array of 10 zeros:")
print(array)


# In[10]:


array=np.ones(10)*5
print("An array of 10 fives:")
print(array)


# ## 5. Create an array of all the even integers from 20 to 35

# In[12]:


for num in range(20,35,2):
  
    print(num)


# ## 6. Create a 3x3 matrix with values ranging from 0 to 8

# In[13]:


import numpy as np
x =  np.arange(0, 9).reshape(3,3)
print(x)


# ## 7. Concatenate a and b 
# ## a = np.array([1, 2, 3]), b = np.array([4, 5, 6])

# In[15]:


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
np.concatenate((a, b), axis=0)


# # Pandas

# ## 8. Create a dataframe with 3 rows and 2 columns

# In[ ]:


import pandas as pd


# In[3]:


data = [['tom', 10], ['nick', 15], ['juli', 14]]
  
# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age'])
  
# print dataframe.
df


# ## 9. Generate the series of dates from 1st Jan, 2023 to 10th Feb, 2023

# In[4]:


from datetime import datetime
pd.date_range(start="2023-01-01",end="2023-02-10").to_pydatetime().tolist()


# ## 10. Create 2D list to DataFrame
# 
# lists = [[1, 'aaa', 22],
#          [2, 'bbb', 25],
#          [3, 'ccc', 24]]

# In[ ]:


lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]


# In[2]:


import pandas as pd
 
# initialize list of lists
lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]
 
# Create the pandas DataFrame
df = pd.DataFrame(lists, columns = ['Index', 'Name', 'Age'])
 
# print dataframe.
print(df )


# In[ ]:




