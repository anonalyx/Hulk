# README

## db_routes file

This file defines a `DB` class which provides methods for interacting with a PostgreSQL database containing tables related to a workout tracking application. The tables and their descriptions are as follows:

### Tables:

1. `account`: Stores user account information.
    - `account_id`: Unique identifier for the user account.
    - `username`: The username of the user.
    - `email`: The email address of the user.

2. `body_part`: Stores information about body parts targeted by exercises.
    - `part_name`: The name of the body part.
    - `calories`: The estimated number of calories burned per minute for exercises targeting this body part.

3. `equipment`: Stores information about workout equipment.
    - `equipment_name`: The name of the equipment.

4. `exercise`: Stores information about specific exercises.
    - `exercise_id`: Unique identifier for the exercise.
    - `exercise_name`: The name of the exercise.
    - `exercise_description`: A description of the exercise.
    - `exercise_body_part`: The body part targeted by the exercise.
    - `exercise_equipment`: The equipment required for the exercise.

5. `favorite`: Stores information about users' favorite exercises.
    - `favorite_id`: Unique identifier for the favorite.
    - `favorite_user`: The username of the user who marked the exercise as a favorite.
    - `favorite_exercise`: The name of the exercise marked as a favorite.

## Functions:

Below is a list of functions provided by the `DB` class. These functions perform various operations on the tables mentioned above:

1. `db_create_tables()`: Creates the tables in the database.

2. `db_populate_records()`: Populates the tables with records from text files.

3. `db_select_all_tables()`: Retrieves and formats all records for each table.

4. `db_select_all_tables_and_records()`: Retrieves and formats all records for each table as a dictionary.

5. `db_select_col_from_table(table, col_index)`: Retrieves a specific column from a table.

6. `db_drop()`: Drops all the tables in the database.

7. `db_get_page_exercise_details(exercise_id)`: Retrieves exercise and body part information based on the exercise id.

8. `db_get_exercise_search_results(part_name, equipment_name, user_id=None)`: Retrieves exercises by body part and equipment criteria and adds a "favorite" flag for the specified user id.

9. `db_register_user(username, email)`: Registers a new user with a username and email address.

10. `db_auth(username, email)`: Authenticates a user by checking if a matching username and email exist in the database.

11. `db_add_favorite_exercise(user_id, exercise_name)`: Adds a new exercise to the user's favorite list in the database.

12. `db_remove_favorite_exercise(user_id, exercise_name)`: Removes a user's favorite exercise from the database based on the user id and exercise name.

13. `db_get_user_favorites(user_id)`: Retrieves the list of favorite exercises for a given user and returns them as a list of dictionaries.
