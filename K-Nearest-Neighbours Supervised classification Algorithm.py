#!/usr/bin/env python
# coding: utf-8

# In[96]:


import numpy as np
from matplotlib import pyplot as plt
from collections import Counter


# In[121]:


def eucledian_distance(x, y):
    return ((x - y) ** 2).sum()

def predict(training_data, labels, test_data, K):
    dis_index = []
    for i in range(training_data.shape[0]):
        #print(i)
        dis = eucledian_distance(training_data[i], test_data)
        #print(dis)
        dis_index.append([dis, labels[i]])
    
    #print(dis_index)
    dis_index.sort()
    dis_index = dis_index[:K]
    dis_index = np.array(dis_index)
    dis_index = dis_index[:,1:2].flatten()
    return Counter(dis_index).most_common(1)[0][0]
    


# In[122]:


x = np.array([[4,3],[22,12], [2, 12], [1, 50]])
y = np.array([1,2,1,2])
pred = np.array([[3,2]])

predict(x, y, pred, 2)


# In[112]:


x = [[4,3],[22,12], [2, 12], [1, 50]]
x = np.array(x)


# In[116]:


x.shape


# In[22]:


a


# In[52]:


from collections import Counter


# In[74]:


a = [[4,3,1],[22,12, 2], [2, 12, 3], [1, 50, 4]]
Counter(a[:,1:2])


# In[95]:


Counter(a[:,1:2].flatten()).most_common(1)[0][0]


# In[84]:


a[:,1:2].flatten()


# In[86]:


dir(Counter(a[:,1:2].flatten()))


# In[88]:


get_ipython().run_line_magic('pinfo', 'Counter.most_common')


# In[ ]:




