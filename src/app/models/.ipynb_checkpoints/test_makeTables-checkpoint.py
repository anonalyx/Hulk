import unittest, sys, os
from make_tables import *

class HulkTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        for table in table_list:
            create(table)

    def tearDown(self):
        drop_all()

    def test_insertion(self):
        value = (23, "LeBron", "Basketball")
        table = "favorite"
        
        insert(value, table)
        with self.assertRaises(sqlite3.IntegrityError):
            insert(value, table)
            
# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()
