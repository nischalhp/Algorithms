from BinarySearchRotatedArray import BinarySearchRotatedArray

from nose.tools import eq_

def test_bsra():
    inp = [3,4,5,6,7,1,2]
    obj = BinarySearchRotatedArray()
    low, low_value, high_value = obj.get_minimum(inp)
    eq_(low_value, 1)
