#!/usr/bin/env python
# coding: utf-8

# In[1]:


def prime(i):
    
    for j in range(2,i):
        
        if i % j == 0:
        
            break
        
    else:
        
        return i

primeNo = filter(prime, range(1, 2500+1))

print ('\nPrime numbers between 1-2500:\n')

print(list(primeNo))


# In[ ]:




