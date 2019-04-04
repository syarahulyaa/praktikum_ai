# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 18:50:04 2019

@author: ASUS
"""

# In[3]: fitur ektraksi
loss, acc = model.evaluate(test_input, test_labels, batch_size=32)
# In[3]: fitur ektraksi
print("Done!")
print("Loss: %.4f, accuracy: %.4f" % (loss, acc))