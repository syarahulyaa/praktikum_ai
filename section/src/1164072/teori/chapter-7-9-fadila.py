# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 20:41:37 2019

@author: ASUS
"""

model = Sequential ()
model.add ( Dense (512, input_shape = (2000,)))
model.add ( Activation ('relu'))
model.add ( Droupout (0.5))
model.add ( Dense (2))
model.add ( Activation ('softmax'))
