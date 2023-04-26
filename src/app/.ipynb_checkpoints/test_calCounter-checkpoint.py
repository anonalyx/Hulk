import unittest, sys, os
from calCounter import *

class TableTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_calories_ex(self):
        tests = [
            [15, 'Bicep Curl', 30]
        ]
        
        testing = Cal_Counter()
        
        for test in tests:
            output = testing.getCalories(test[0], test[1])
            self.assertEqual(output, test[2])
            
    def test_calories_body(self):
        tests = [
            [15, 'Arms', 30]
        ]
        
        testing = Cal_Counter()
        
        for test in tests:
            output = testing.getCalories(test[0], bodyPart = test[1])
            self.assertEqual(output, test[2])
            
# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()