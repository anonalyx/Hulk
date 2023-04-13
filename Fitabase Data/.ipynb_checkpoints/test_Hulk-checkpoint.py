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
        def testSample(data, columns, seed):
            sample_size = 10000

            data_sample = data[columns].sample(
                n = sample_size, replace = True, random_state = seed
            )

            data_sample = data_sample.groupby(columns[0])
            data_sample = data_sample.sum()

            return data_sample
        
        def testCal(calories):
            try:
                distance = target(calories, test_model)
                return int(distance)

            except:
                return 0
        
        seed = 3308
        test_data = testSample(fit, columns, seed)

        test_model = smf.ols(
            formula = 'Calories ~ TotalSteps', 
            data = test_data
        ).fit()
        
        tests = {
            475000: [380235, "380235 steps to burn 475000 calories"],
            "42000": [0, "string input causes exception returning 0"],
            -2.5: [0, "negative output should return 0"]
        }
        
        for test, expect in tests.items():
            output = testCal(test)
            self.assertEqual(output, expect[0], expect[1])
            
# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()
