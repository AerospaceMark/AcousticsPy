import unittest
from acousticspy.decibels import add_decibels
from acousticspy.decibels import dB_to_pressure
import numpy as np

# To run these tests, make sure that you're in the top of the "acoustics" package and run:
# "python -m unittest discover -v tests/"

class TestAddDecibels(unittest.TestCase):

    #--------------------------------------
    # Testing the `add_decibels()` function
    #--------------------------------------

    def test_add_decibels_normal(self):
        value = add_decibels([1,1])
        expected = 4.010299956639813
        decimalPlaces = 12
        message = "Results are not equal within 12 digits"
        delta = None # Could also say: delta = 1e-12. Must specify decimalPlaces or delta, but not both
        self.assertAlmostEqual(value,expected,decimalPlaces,message,delta)

    def test_add_decibels_coherent(self):
        value = add_decibels([1,1],coherent = True)
        expected = 7.020599913279622
        decimalPlaces = 12
        message = "Results are not equal within 12 digits"
        delta = None # Could also say: delta = 1e-12. Must specify decimalPlaces or delta, but not both
        self.assertAlmostEqual(value,expected,decimalPlaces,message,delta)

    def test_add_decibels_incoherent(self):
        value = add_decibels([1,1],coherent = False)
        expected = 4.010299956639813
        decimalPlaces = 12
        message = "Results are not equal within 12 digits"
        delta = None # Could also say: delta = 1e-12. Must specify decimalPlaces or delta, but not both
        self.assertAlmostEqual(value,expected,decimalPlaces,message,delta)

class TestDBToPressure(unittest.TestCase):
    
    #---------------------------------------
    # Testing the dB_to_pressure() function
    #---------------------------------------

    def test_dB_to_pressure(self):
        value = dB_to_pressure(94,20e-6)
        expected = 1.0023744672545452
        decimalPlaces = 12
        message = "Results are not equal within 12 digits"
        delta = None
        self.assertAlmostEqual(value,expected,decimalPlaces,message,delta)

    def test_dB_to_pressure_0_dB(self):
        value = dB_to_pressure(0,1)
        expected = 1.0
        decimalPlaces = 12
        message = "Results are note equal within 12 digits"
        delta = None
        self.assertAlmostEqual(value,expected,decimalPlaces,message,delta)

if __name__ == "__main__":
    print("Decibels Passed")
