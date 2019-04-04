# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 13:03:18 2019

@author: lsvapr
"""

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
print(model.summary())