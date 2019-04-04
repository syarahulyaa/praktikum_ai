# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 13:03:18 2019

@author: lsvapr
"""

model = Sequential([
    Dense(100, input_dim=np.shape(train_input)[1]),
    Activation('relu'),
    Dense(10),
    Activation('softmax'),
    ])