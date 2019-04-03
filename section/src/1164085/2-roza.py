# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 21:04:16 2019

@author: ASUS
"""

def display_mfcc(song):
    y, _ = librosa.load(song)
    mfcc = librosa.feature.mfcc(y)

    plt.figure(figsize=(10, 4))
    librosa.display.specshow(mfcc, x_axis='time', y_axis='mel')
    plt.colorbar()
    plt.title(song)
    plt.tight_layout()
    plt.show()
display_mfcc('genres/classical/classical.00067.au')