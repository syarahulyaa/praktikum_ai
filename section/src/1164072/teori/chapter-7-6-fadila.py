# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 21:02:04 2019

@author: ASUS
"""

from keras.preprocessing.text import Tokenizer

tokenizer = Tokenizer(num_words = 3)
texts = ['a b b c c c', 'a b c']
tokenizer.fit_on_texts(texts)
print(tokenizer.texts_to_matrix(texts, mode='count'))