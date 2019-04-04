# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 18:50:04 2019

@author: ASUS
"""

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
print(model.summary())