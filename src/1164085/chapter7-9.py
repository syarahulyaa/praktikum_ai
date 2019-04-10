# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 19:59:26 2019

@author: ASUS
"""

model = Sequential()
       	model.add(Dense(512, input_shape=(2000,)))
       	model.add(Activation('relu'))
       	model.add(Dropout(0.5))
       	model.add(Dense(2))
       	model.add(Activation('softmax'))