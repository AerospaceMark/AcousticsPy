# This contains code that enables decibel math

import numpy as np

def add_decibels(x,coherent = False):
    
    if coherent:
        summation = 20 * np.log10(sum(10**(x/10)))
    else:
        summation = 10 * np.log10(sum(10**(x/10)))

    return summation
