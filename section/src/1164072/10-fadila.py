# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 19:18:28 2019

@author: ASUS
"""


loss, acc = model.evaluate(test_input, test_labels, batch_size=32)
#%%
print("Done!")
print("Loss: %.4f, accuracy: %.4f" % (loss, acc))
