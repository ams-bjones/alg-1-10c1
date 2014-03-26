import heron
import unittest

class TestSequenceFunctions(unittest.TestCase):
    
    def test1(self):
        triangle = [3,4,5]
        expsemi = 6
        assert heron.semi(triangle) == expsemi #Test 1 fails
        
    def test2(self):
        triangle = [3,4,5]
        semi = 6
        expAword = 6
        assert heron.aword(semi, triangle) == expAword #Test 2 fails
    
    def test3(self):
        triangle = [3,4,5]
        Area = 6
        assert heron.area(triangle) == Area #Test 3 fails



if __name__ == '__main__':
    unittest.main()