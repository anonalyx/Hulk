import unittest
from Hulk import *

class HulkTest(unittest.TestCase):

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

    def test_calories(self):
        tests = {
            42000: [1215, "1215 step to burn 42000 calories"],
            "42000": [0, "string input causes exception returning 0"],
            -2.5: [0, "negative output should return 0"]
        }
        
        for test, expect in tests.items():
            output = calCalc(test)
            self.assertEqual(output, expect[0], expect[1])
            
# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()
