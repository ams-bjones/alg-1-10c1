#testing min and max functions
import minMax
import unittest

class TestSequenceFunctions(unittest.TestCase):



    def test1(self):
        input1 = [10,9,8,7,6,5] 
        assert minMax.min(input1)==5 #Test 1 fails
        
    def test2(self):
        input2 = [4,5,6,7,8,9,10]
        assert minMax.min(input2)==4 #Test 2 fails
    
    def test3(self):
        input1 = [10,9,8,7,6,5] 
        assert minMax.max(input1)==10 #Test 3 fails

    def test4(self):
        input2 = [4,5,6,7,8,9,10] 
        assert minMax.max(input2)==10 #Test 4 fails


if __name__ == '__main__':
    unittest.main()