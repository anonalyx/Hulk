
# SQL Design

## Team 2 - Project Hulk

---

### Table: body_part

A table to hold all body parts that can be targeted by exercises in the database

**Attributes:**

- **part_id**: a unique integer id, primary key
- part_name: the name of the body part, a variable-length string 30 characters maximum
- calories: an integer representing the approximate number of calories burned by exercises targeting the body part

**Tests:**

- data types for part_id and calories must be integer
- part_name data type must be string
- unit tests for incorrect data types should raise exception
- tests for invalid numbers, such as negative values and decimal floats, expected to return error
- testing for part_name will include empty string as well as string length exceeding 30 characters


---

### Table: equipment

A table to hold all the equipment necessary to perform exercises in the database 

**Attributes:**

- **equipment_id**: a unique integer id, primary key
- equipment_name: the name of the equipment, a unique variable-length string 30 characters maximum

**Tests:**

- data type for equipment_id must be integer and equipment_name must be string
- unit tests for incorrect data types should raise exception
- tests for invalid numbers, such as negative values and decimal floats, expected to return error
- testing for equipment_name will include empty string as well as string length exceeding 30 characters

---

### Table: exercise

A table to hold information about all exercises in the database 

**Attributes:**

- **exercise_id**: a unique integer id, primary key
- exercise_name: the name of the exercise, a unique variable-length string 30 characters maximum
- exercise_description: a brief description of the exercise and how to perform it, a variable-length string 1000 characters maximum
- exercise_body_part: a foreign key to the body_part table, indicates which (primary) body part the exercise targets
- exercise_equipment: a foreign key to the equipment table, indicates what equipment is necessary to perform the exercise

**Tests:**

- data type for exercise_id  must be integer 
- data type for exercise_name and exercise_description must be string
- unit tests for incorrect data types should raise exception
- tests for invalid numbers, such as negative values and decimal floats, expected to return error
- testing for strings will include empty string as well as string length exceeding maximum
- foreign keys for exercise_body_part and exercise_equipment must exist in respective tables

---

### Table: user

A table to hold all registered users, used for login function and to track favorite exercises

**Attributes:**

- **user_id**: a unique integer id, primary key
- username: an alias chosen by the user, a unique variable-length string 15 characters maximum
- email: the user's email address, a unique variable-length string 320 characters maximum; must adhere to email address format

**Tests:**

- data type for user_id  must be integer 
- data type for username and email must be string
- unit tests for incorrect data types should raise exception
- tests for invalid numbers, such as negative values and decimal floats, expected to return error
- testing for username will include empty string as well as string length exceeding 15 characters
- email addresses will be tested for proper format using regular expressions

---

### Table: favorite

A table to hold the many-to-many relationship between users and their favorite exercises

**Attributes:**

- **favorite_id**: a unique integer id, primary key
- favorite_user: a foreign key to the user table, indicates which user the favorite is associated with
- favorite_exercise: a foreign key to the exercise table, indicates which exercise the user has added as a favorite

**Tests:**

- data type for favorite_id  must be integer
- unit tests for incorrect data types should raise exception
- tests for invalid numbers, such as negative values and decimal floats, expected to return error
- foreign keys for favorite_user and favorite_exercise must exist in respective tables

---

### Method: Exercise Search

Given a user's selections of body part(s) and equipment, returns the exercises that target the given body part and do not require any equipment beyond the selection given (exercises that target a body part but do not require any equipment should be returned regardless of what equipment is selected). Will query the exercise, equipment, and body_part tables to find exercises that match, then if the user is logged in will query the favorites table to check if any of the exercise results are in the user's favorites.

**Parameters:**
- array of body parts generated from user input form (part_name)
- array of equipment generated from user input form (equipment_name)
- user_id if a user is currently logged in

**Return values:**
- array of exercises that match criteria, each formatted as a dictionary with exercise_id, exercise_name, part_name, equipment_name, and a boolean value for favorite

**Tests:**

- input arrays must contain valid part_name and equipment_name values
- user_id must correspond to registered user
- invalid input parameters should cause error
- proper input parameters expected to return correct array of exercises

---

### Method: Get Exercise Details

Given an exercise, returns the full details of the exercise. Queries the exercise, equipment, and body_part tables for exercise and calorie information.

**Parameters:**
- exercise_id

**Return values:**
- dictionary of exercise_name, exercise_description, body_part_name, equipment_name, calories

**Tests:**

- data type for exercise_id must be integer
- unit tests for incorrect data types should raise exception
- tests for invalid numbers, such as negative values and decimal floats, expected to return error
- exercise_id parameter must exist in exercise table
- valid input parameters expected to return correct dictionary values

---

### Method: Register User

Create a new entry in the user table given user input. Will query the user table to verify that username and email address are not already used for an account; format and length validation will be handled on the client side. If the username and email do not already exist in the table, a new entry will be added.

**Parameters:**
- username string from user input
- email address string from user input

**Return values:**
- success or failure indicator
- error message if failure

**Tests:**

- data types for username and email address must be strings
- unit tests for incorrect data types should raise exception
- testing for username and email address will include empty strings
- email addresses will be tested for proper format using regular expressions
- invalid strings and preexisting entries expected to return failure message
- when a new entry is successfully added, return value should be True

---

### Method: Login

Log a user in by setting the session variable user_id given a valid username and email combination. Queries the user table to find a matching entry and retrieve user_id.

**Parameters:**
- username string from user input
- email address string from user input

**Return values:**
- success or failure indicator
- error message if failure

**Tests:**

- data types for username and email address must be strings
- unit tests for incorrect data types should raise exception
- testing for username and email address will include empty strings
- email addresses will be tested for proper format using regular expressions
- username and email address must both exist in user table
- invalid strings and nonexistent entries expected to return failure message
- when user is successfully logged in, return value should be True

---

### Method: Add Favorite Exercise

Given a user is logged in, add an exercise to their favorites by creating a new entry in the favorite table. Queries the favorite table to check if an entry for the user and exercise exists, and adds an entry if none exists.

**Parameters:**
- user_id from session
- exercise_id from user input (button)

**Return values:**
- success or failure indicator
- error message if failure

**Tests:**

- data types for user_id and exercise_id must be integers
- unit tests for incorrect data types should raise exception
- tests for invalid numbers, such as negative values and decimal floats, expected to return error
- user_id must exist in user table and exercise_id must exist in exercise table
- invalid id parameters and preexisting favorite entries expected to return failure message
- when a new favorite exercise is successfully added, return value should be True

---

### Method: Remove Favorite Exercise

Given a user is logged in, remove an exercise from their favorites by removing the entry in the favorite table. Queries the favorite table to check if an entry for the user and exercise exists, and if so removes it.

**Parameters:**
- user_id from session
- exercise_id from user input (button)

**Return values:**
- success or failure indicator
- error message if failure

**Tests:**

- data types for user_id and exercise_id must be integers
- unit tests for incorrect data types should raise exception
- tests for invalid numbers, such as negative values and decimal floats, expected to return error
- user_id must exist in user table and exercise_id must exist in exercise table
- invalid id parameters and nonexistent favorite entries expected to return failure message
- when an old favorite exercise is successfully removed, return value should be True

---

### Method: Get User Favorites

Given a user is logged in, return the exercises they have added to their favorites. Queries the favorite table for the user's entries and the exercise table for exercise details.

**Parameters:**
- user_id from session

**Return values:**
- array of exercises that match criteria, each formatted as a dictionary with exercise_id, exercise_name, part_name, equipment_name

**Tests:**

- data type for user_id must be integer
- unit tests for incorrect data types should raise exception
- tests for invalid numbers, such as negative values and decimal floats, expected to return error
- user_id parameter must exist in user table
- valid id parameters expected to return favorite exercises
