# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 19:01:33 2019

@author: lsvapr
"""

d_train_inputs = tokenizer.texts_to_matrix(train_content, mode='tfidf')
d_test_inputs = tokenizer.texts_to_matrix(test_content, mode='tfidf')