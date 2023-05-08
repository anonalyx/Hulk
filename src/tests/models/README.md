# README

## Test Suite for Workout Tracking Application

This file contains a series of unit tests for the workout tracking application. These tests are designed to ensure the correct functionality of the application, specifically with regards to database interactions and manipulation.

### File Contents

1. `TestDB`: The main test class, which is a subclass of the `unittest.TestCase` class.

### Test Methods

1. `setUpClass()`: Sets up the testing environment, including initializing a test database and populating it with test data.

2. `tearDownClass()`: Cleans up the testing environment, including deleting the test database.

3. `setUp()`: Sets up the test case.

4. `tearDown()`: Cleans up the test case.

5. `test_db_create_tables()`: Tests the `db_create_tables()` method in the `DB` class.

6. `test_select_all_tables()`: Tests the `db_select_all_tables()` method in the `DB` class.

7. `test_populate_records()`: Tests the `db_populate_records()` method in the `DB` class.

8. `test_db_inserting()`: Tests the `db_inserting()` method in the `DB` class.

9. `test_db_selecting()`: Tests the `db_selecting()` method in the `DB` class.

10. `test_db_get_page_exercise_details()`: Tests the `db_get_page_exercise_details()` method in the `DB` class.

11. `test_db_get_exercise_search_results()`: Tests the `db_get_exercise_search_results()` method in the `DB` class.

12. `test_get_page_search_results()`: Tests the `get_page_search_results()` function in the application.

13. `test_get_search_results()`: Tests the `get_search()` function in the application.

14. `test_register_user()`: Tests the `register_user()` function in the application.

15. `test_add_favorite_exercise()`: Tests the `add_favorite_exercise()` function in the application.

16. `test_remove_favorite_exercise()`: Tests the `remove_favorite_exercise()` function in the application.

To run the test suite, execute the following command:

