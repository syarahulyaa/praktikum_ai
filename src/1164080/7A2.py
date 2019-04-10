# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 19:01:33 2019

@author: lsvapr
"""

kfold = StratifiedKFold(n_splits=5)
splits = kfold.split(d, d['CLASS'])