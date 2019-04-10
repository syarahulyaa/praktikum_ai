# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 19:01:33 2019

@author: lsvapr
"""

d_train_outputs = np_utils.to_categorical(d['CLASS'].iloc[train_idx])
d_test_outputs = np_utils.to_categorical(d['CLASS'].iloc[test_idx])