# This contains code that enables decibel math

import numpy as np

def add_decibels(dB,coherent = False):
    
    if coherent:
        summation = 20 * np.log10(sum(10**(dB/20)))
    else:
        summation = 10 * np.log10(sum(10**(dB/10)))

    return summation
