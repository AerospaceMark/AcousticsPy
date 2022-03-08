import numpy as np
import scipy.special as sp

def baffled_circular_piston_directivity(radius,frequency,theta):
    c = 343
    k = 2*np.pi*frequency/c
    return 2*sp.jv(1,k*radius*np.sin(theta)) / (k*radius*np.sin(theta))

def get_circle_elements(total_area,num_elements):
    
    radius = np.sqrt(total_area/np.pi)
    
    dx = 2*radius/num_elements
    areas = np.zeros(num_elements)
    positions = np.zeros(num_elements)
    
    for i in range(num_elements):
        x = (dx*i - radius) + dx/2
        y = np.sqrt(radius**2 - x**2)
        areas[i] = 2*y*dx
        positions[i] = x
        
    return positions, areas

def get_square_elements(total_area,num_elements):
    
    half_length = np.sqrt(total_area)/2
    
    dx = 2*half_length/num_elements
    areas = np.zeros(num_elements)
    positions = np.zeros(num_elements)
    
    for i in range(num_elements):
        x = (dx*i - half_length) + dx/2
        y = half_length
        areas[i] = 2*y*dx
        positions[i] = x
        
    return positions, areas