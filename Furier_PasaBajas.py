#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
from skimage.io import imread
import matplotlib.pyplot as plt
import scipy.fftpack as fp


# In[5]:


im = np.mean(imread('Captura.jpg'), axis=2) # assuming an RGB image
plt.figure(figsize=(10,10))
plt.imshow(im, cmap=plt.cm.gray)
plt.axis('off')
plt.show()


# In[9]:


F1 = fp.fft2((im).astype(float))
F2 = fp.fftshift(F1)
plt.figure(figsize=(10,10))
plt.imshow( (20*np.log10( 0.1 + F2)).astype(int), cmap=plt.cm.gray)
plt.show()


# In[10]:


(w, h) = im.shape
half_w, half_h = int(w/2), int(h/2)

# high pass filter
n = 25
F2[half_w-n:half_w+n+1,half_h-n:half_h+n+1] = 0 # select all but the first 50x50 (low) frequencies
plt.figure(figsize=(10,10))
plt.imshow( (20*np.log10( 0.1 + F2)).astype(int))
plt.show()


# In[12]:


im1 = fp.ifft2(fp.ifftshift(F2)).real
plt.figure(figsize=(10,10))
plt.imshow(im1, cmap='gray')
plt.axis('off')
plt.show()


# In[ ]:




