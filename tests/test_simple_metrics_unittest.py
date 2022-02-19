import unittest
from acoustics.metrics import get_oaspl

import numpy as np

# To run these tests, make sure that you're in the top of the "acoustics" package and run:
# "python -m unittest discover -v tests/"

class TestGetOASPL(unittest.TestCase):

    #-----------------------------------
    # Testing the `get_oaspl()` function
    #-----------------------------------

    def test_get_oaspl_normal(self):
        # Create a long array with a standard deviation of 1.0
        x = np.random.randn(1000000)
        value = get_oaspl(x)
        expected = 93.97940008672037
        decimalPlaces = 1
        message = "Failure with std(x) = 1"
        delta = None
        self.assertAlmostEqual(value,expected,decimalPlaces,message,delta)

if __name__ == "__main__":
    test_simple_metrics()
    print("Everything Passed")
