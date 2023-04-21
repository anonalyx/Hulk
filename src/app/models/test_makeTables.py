import unittest, sys, os
from make_tables import *

class TableTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        conn, c = connect("testing_tables")
        
        for table in table_list:
            create(table)

    def tearDown(self):
        drop_all()

    def test_dupe(self):
        tests = {
            "account": (3308, "LeBron James", "KingJames@nba.com"),
            "body_part": (69, "Gluteus Maximus", "Squats"),
            "equipment": (777, "Vibrator"),
            "exercise": (3173, "One Punch Man", 
                         "100 situps, pushups, and squats followed by a 10-mile run",
                         "Arms", "Dumbells"),
            "favorite": (23, 'LeBron', 'Basketball')
        }
        
        for table, value in tests.items():
            insert(value, table)
            
            with self.assertRaises(sqlite3.IntegrityError):
                insert(value, table)
            
# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()
