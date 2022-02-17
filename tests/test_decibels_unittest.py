import unittest
from acoustics.decibels import add_decibels
import numpy as np

# To run these tests, make sure that you're in the top of the "acoustics" package and run:
# "python -m unittest -v tests/test_decibels_unittest.py"

class TestAddDecibels(unittest.TestCase):
    def test_add_decibels_normal(self):
        value = add_decibels(np.array([1,1]))
        expected = 4.010299956639813
        decimalPlaces = 12
        message = "Results are not equal within 12 digits"
        delta = None # Could also say: delta = 1e-12. Must specify decimalPlaces or delta, but not both
        self.assertAlmostEqual(value,expected,decimalPlaces,message,delta)

    def test_add_decibels_coherent(self):
        value = add_decibels(np.array([1,1]),coherent = True)
        expected = 7.020599913279622
        decimalPlaces = 12
        message = "Results are not equal within 12 digits"
        delta = None # Could also say: delta = 1e-12. Must specify decimalPlaces or delta, but not both
        self.assertAlmostEqual(value,expected,decimalPlaces,message,delta)

    def test_add_decibels_incoherent(self):
        value = add_decibels(np.array([1,1]),coherent = False)
        expected = 4.010299956639813
        decimalPlaces = 12
        message = "Results are not equal within 12 digits"
        delta = None # Could also say: delta = 1e-12. Must specify decimalPlaces or delta, but not both
        self.assertAlmostEqual(value,expected,decimalPlaces,message,delta)


if __name__ == "__main__":
    test_add_decibels()
    print("Everything Passed")
