#!/usr/bin/env python
# coding: utf-8

# In[49]:


answer = [None, None]

def f(A, U):
    if(U != set()):
        x = U.pop()
        f(A.union([x]), U.union(set()))
        f(A.union(set()), U.union(set()))
    else:
        global answer
        if(sum(A) == 20):
            if(answer[0] == None or len(A) < answer[0]):
                answer[0] = len(A)
                answer[1] = A
            
        print("len =", len(A),A, "sum =", sum(A))


# In[50]:


A = set()
U = {1,4,5,8,11}


# In[53]:


f(A,U)
print(answer)


# In[52]:


answer


# In[ ]:




