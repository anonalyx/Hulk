import unittest
import requests
from src.app.models.db_routes import DB
from src.app.app import get_page_search_results, get_search


class TestDB(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = DB(isTest=True, isLocal=True)
        cls.exercise_id = 1
        cls.part_name = 'Arms'
        cls.equipment_name = 'Dumbbells'
        cls.user_id = 23
        with cls.db as x:
            x.db_drop()
            x.db_create_tables()
            x.db_populate_records()
            print(f'should not be empty: {x.db_select_all_tables_and_records()}')
    @classmethod
    def tearDownClass(cls):
        cls.db.db_drop()

    def setUp(self):
        pass




    def tearDown(self):
        pass

    def test_db_create_tables(self):
        with self.db as x:
            table_names = set([record[1] for record in x.db_select_all_tables() if record[1][0:4] == 'test'])
        self.assertEqual({'test_account', 'test_body_part', 'test_equipment', 'test_exercise', 'test_favorite'},
                         table_names)

    def test_select_all_tables(self):
        with self.db as x:
            x.db_select_all_tables()
        table_names = set([record[1] for record in self.db.db_select_all_tables() if record[1][0:4] == 'test'])
        self.assertEqual({'test_account', 'test_body_part', 'test_equipment', 'test_exercise', 'test_favorite'},
                         table_names)

    def test_populate_records(self):
        with self.db as x:
            x.db_populate_records()
            records = x.db_select_all_tables_and_records()
        self.assertEqual(len(records), 5)

    def test_db_inserting(self):
        with self.db as x:
            x.db_inserting()
        self.assertEqual(self.db.cur.execute.call_count, len(self.db.tables))

    def test_db_selecting(self):
        with self.db as x:
            x.cur.fetchall.return_value = [('test data',)]
        result = self.db.db_selecting()
        self.assertIn('test data', result)

    def test_db_get_page_exercise_details(self):
        with self.db as x:
            result = x.db_get_page_exercise_details(self.exercise_id)
        self.assertCountEqual(result.keys(),
                              ['exercise_name', 'exercise_description', 'body_part_name', 'equipment_name', 'calories'])

        # Check that each value in the dictionary is not None
        for key in result:
            self.assertIsNotNone(result[key])

    def test_db_get_exercise_search_results(self):

        with self.db as x:
            result = x.db_get_exercise_search_results(self.part_name, self.equipment_name, self.user_id)
        for item in result:
            self.assertIsInstance(item, dict)
            self.assertCountEqual(item.keys(),
                                  ['exercise_id', 'exercise_name', 'part_name', 'equipment_name', 'favorite'])

            # Check that each value in the dictionary is not None
            for key in item:
                self.assertIsNotNone(item[key])

    def test_get_page_search_results(self):

        data = get_page_search_results(self.part_name, self.equipment_name)
        print(data)
    def test_get_search_results(self):
        get_search()

if __name__ == '__main__':
    unittest.main()
