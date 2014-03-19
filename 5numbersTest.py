#tests for 5 numbers

import fiveNumbers
import unittest

class TestSequenceFunctions(unittest.TestCase):

   

    def test1(self):
        numbers = [1,1,1,1,1]
        answer = 5
        assert fiveNumbers.total(numbers) == answer # a list of 5 1's does not evaluate correctly.
    
    def test2(self):
        numbers = [1,2,3,4,5]
        answer = 15
        assert fiveNumbers.total(numbers) == answer # test 2 fails

   

if __name__ == '__main__':
    unittest.main()