# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 19:01:33 2019

@author: lsvapr
"""

d_train_inputs = d_train_inputs/np.amax(np.absolute(d_train_inputs))
d_test_inputs = d_test_inputs/np.amax(np.absolute(d_test_inputs))