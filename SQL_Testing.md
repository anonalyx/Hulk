
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


---

### Table: equipment

A table to hold all the equipment necessary to perform exercises in the database 

**Attributes:**
  
- **equipment_id**: a unique integer id, primary key
- equipment_name: the name of the equipment, a unique variable-length string 30 characters maximum

**Tests:**

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

---

### Table: user

A table to hold all registered users, used for login function and to track favorite exercises

**Attributes:**
  
- **user_id**: a unique integer id, primary key
- username: an alias chosen by the user, a unique variable-length string 15 characters maximum
- email: the user's email address, a unique variable-length string 320 characters maximum; must adhere to email address format

**Tests:**

---

### Table: favorite

A table to hold the many-to-many relationship between users and their favorite exercises

**Attributes:**
  
- **favorite_id**: a unique integer id, primary key
- favorite_user: a foreign key to the user table, indicates which user the favorite is associated with
- favorite_exercise: a foreign key to the exercise table, indicates which exercise the user has added as a favorite

**Tests:**

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

---

### Method: Get Exercise Details

Given an exercise, returns the full details of the exercise. Queries the exercise, equipment, and body_part tables for exercise and calorie information.

**Parameters:**
- exercise_id

**Return values:**
- dictionary of exercise_name, exercise_description, body_part_name, equipment_name, calories

**Tests:**

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

---

### Method: Get User Favorites

Given a user is logged in, return the exercises they have added to their favorites. Queries the favorite table for the user's entries and the exercise table for exercise details.

**Parameters:**
- user_id from session

**Return values:**
- array of exercises that match criteria, each formatted as a dictionary with exercise_id, exercise_name, part_name, equipment_name

**Tests:**
