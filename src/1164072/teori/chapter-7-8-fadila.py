# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 21:18:02 2019

@author: ASUS
"""

y_train = [1, 0, 3, 4, 5, 0, 2, 1]

#%%

np_utils.to_categorical(y_train, num_classes=6)
