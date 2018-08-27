
# coding: utf-8

# In[1]:


import numpy as np
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


# ### Crear Vectores uni-, bi- o multi- dimensionales 

# In[6]:


np.array([1,2,3,4])


# In[7]:


np.array([[1,2],[3,4], [5,6]])


# In[8]:


np.array([[[1,2,3], [1,2,3]],[[1,2,3], [1,2,3]], [[1,2,3], [1,2,3]]])


# ### Vector cero

# In[9]:


np.zeros(3)


# In[10]:


np.zeros((2,3))


# In[11]:


np.zeros((2,3,4))


# ### Dimensión de Arrays

# In[12]:


np.shape(np.array([1,2,3,4]))


# ### Acceso a Arrays

# In[25]:


x = np.array([[1,2],[3,4], [5,6]])
x[0]
x[0,1]


# In[22]:


np.array([[1,2,3,4],[3,4,5,6], [2,3,3,4]])[0:3]


# ### Operaciones

# In[40]:


x = np.array([[1,2,3,4],[3,4,5,6]])
np.sum(x)
np.sum(x, axis=1)
x - x
x - x[1]
np.abs(x - x[1])


# In[45]:


x = np.array([[[1,2,3],[3,4,5]], [[1,2,3], [3,4,5]]])
np.sum(x, axis=0)
np.sum(x, axis=1)
np.sum(x, axis=2)


# In[47]:


np.argmin(np.array([13,11,12]))

