# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 18:50:04 2019

@author: ASUS
"""

model = Sequential([
    Dense(100, input_dim=np.shape(train_input)[1]),
    Activation('relu'),
    Dense(10),
    Activation('softmax'),
    ])