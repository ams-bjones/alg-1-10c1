#testing the triangle file
import triangle
import unittest

class TestSequenceFunctions(unittest.TestCase):



    def test1(self):
        width = 4
        height = 12
        area = 24
        assert triangle.area(width, height) == area #Test 1 fails
        
    def test2(self):
        width = 6
        height = 2
        area = 6
        assert triangle.area(width, height) == area #Test 2 fails


if __name__ == '__main__':
    unittest.main()