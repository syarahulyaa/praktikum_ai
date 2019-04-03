# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 19:13:34 2019

@author: ASUS
"""

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
print(model.summary())