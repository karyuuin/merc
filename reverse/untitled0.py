# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 10:11:35 2018

@author: class
"""



from scipy.io.wavfile import read
from scipy.io.wavfile import write
import numpy as np
from scipy.io import wavfile

fs, data = read('queen_-_bohemian-rhapsody.wav')
print(data)
data = data[::-1]
print(data)
write('uu.wav',fs,data)