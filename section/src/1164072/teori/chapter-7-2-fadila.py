# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 20:43:01 2019

@author: ASUS
"""

kfold = StratifiedKFold(n_splits=5)
splits = kfold.split(d, d['CLASS'])