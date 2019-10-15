#!/usr/bin/env python
# coding: utf-8

# In[1]:


revenue = {
    1 : 1,
    2 : 5,
    3 : 8,
    4 : 9,
    5 : 10,
    6 : 17,
    7 : 17,
    8 : 20
}

mem = {
    1 : None,
    2 : None,
    3 : None,
    4 : None,
    5 : None,
    6 : None,
    7 : None,
    8 : None
}

#fun(inch) = (i, fun(inch-i))
tab = {
    1 : None,
    2 : None,
    3 : None,
    4 : None,
    5 : None,
    6 : None,
    7 : None,
    8 : None
}


# In[2]:


def fun(inch):
    if(mem[inch]):
        return mem[inch]
    
    max_revenue = revenue[inch]
    tab[inch] = inch
    for i in range(1,inch):
        _ = revenue[i] + fun(inch - i)
        if(_ > max_revenue):
            tab[inch] = i
            max_revenue = _
    #print(tab[inch])
    mem[inch] = max_revenue
    return max_revenue


# In[3]:


print("Max Revenue =", fun(8))


# In[ ]:




