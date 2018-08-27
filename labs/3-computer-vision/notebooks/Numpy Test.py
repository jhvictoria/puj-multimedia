
# coding: utf-8

# In[48]:


import numpy as np


# ### Crear Vectores uni-, bi- o multi- dimensionales 

# In[49]:


np.array([1,2,3,4])


# In[50]:


np.array([[1,2],[3,4], [5,6]])


# In[51]:


np.array([[[1,2,3], [1,2,3]],[[1,2,3], [1,2,3]], [[1,2,3], [1,2,3]]])


# ### Vector cero

# In[52]:


np.zeros(3)


# In[53]:


np.zeros((2,3))


# In[54]:


np.zeros((2,3,4))


# ### Dimensión de Arrays

# In[55]:


np.shape(np.array([1,2,3,4]))


# ### Acceso a Arrays

# In[56]:


x = np.array([[1,2],[3,4], [5,6]])
x[0]
x[0,1]


# In[57]:


np.array([[1,2,3,4],[3,4,5,6], [2,3,3,4]])[0:3]


# ### Operaciones

# In[58]:


x = np.array([[1,2,3,4],[3,4,5,6]])
np.sum(x)
np.sum(x, axis=1)
x - x
x - x[1]
np.abs(x - x[1])


# In[59]:


x = np.array([[[1,2,3],[3,4,5]], [[1,2,3], [3,4,5]]])
np.sum(x, axis=0)
np.sum(x, axis=1)
np.sum(x, axis=2)


# In[60]:


np.argmin(np.array([13,11,12]))


# In[61]:


get_ipython().system('ipython nbconvert --to=python "Numpy Test.ipynb"')

