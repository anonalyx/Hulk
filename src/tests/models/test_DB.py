import unittest
from src.app.models.db_routes import DB


class TestDB(unittest.TestCase):

    def setUp(self):
        self.db = DB(isTest=True, isLocal=True)
        self.exercise_id = 1
        self.part_name = 'Arms'
        self.equipment_name = 'Dumbbells'
        self.user_id = 23
        self.db.db_drop()

    def tearDown(self):
        self.db.db_drop()

    def test_db_create_tables(self):
        self.db.db_create_tables()
        table_names = set([record[1] for record in self.db.db_select_all_tables() if record[1][0:4] == 'test'])
        self.assertEqual({'test_account', 'test_body_part', 'test_equipment', 'test_exercise', 'test_favorite'},
                         table_names)

    def test_select_all_tables(self):
        self.db.db_select_all_tables()
        table_names = set([record[1] for record in self.db.db_select_all_tables() if record[1][0:4] == 'test'])
        self.assertEqual({'test_account', 'test_body_part', 'test_equipment', 'test_exercise', 'test_favorite'},
                         table_names)

    def test_populate_records(self):
        self.db.db_populate_records()
        records = self.db.db_select_all_tables_and_records()
        self.assertEqual(len(records), 5)

    def test_db_inserting(self):
        self.db.db_inserting()
        self.assertEqual(self.db.cur.execute.call_count, len(self.db.tables))

    def test_db_selecting(self):
        self.db.cur.fetchall.return_value = [('test data',)]
        result = self.db.db_selecting()
        self.assertIn('test data', result)

    def test_db_get_page_exercise_details(self):
        result = self.db.db_get_page_exercise_details(self.exercise_id)
        self.assertCountEqual(result.keys(),
                              ['exercise_name', 'exercise_description', 'body_part_name', 'equipment_name', 'calories'])

        # Check that each value in the dictionary is not None
        for key in result:
            self.assertIsNotNone(result[key])

    def test_db_get_page_exercise_search(self):
        self.db.db_create_tables()
        self.db.db_populate_records()
        result = self.db.db_get_page_exercise_search(self.part_name, self.equipment_name, self.user_id)
        for item in result:
            self.assertIsInstance(item, dict)
            self.assertCountEqual(item.keys(),
                                  ['exercise_id', 'exercise_name', 'part_name', 'equipment_name', 'favorite'])

            # Check that each value in the dictionary is not None
            for key in item:
                self.assertIsNotNone(item[key])

if __name__ == '__main__':
    unittest.main()
