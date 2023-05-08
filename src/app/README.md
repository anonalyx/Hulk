# README

This is a simple Flask app that allows users to calculate steps required to burn a certain amount of calories, search for exercises based on body part and equipment, and manage their favorite exercises. Users need to log in or sign up to access the application.

## Routes

### `/`

- Method: `GET`
- Description: Renders the login page.

### `/auth`

- Method: `POST`
- Description: Authenticates the user by checking the provided username and email against the database.
- Input: `username`, `email`

### `/signup`

- Method: `POST`
- Description: Registers a new user by adding the provided username and email to the database.
- Input: `username`, `email`

### `/home`

- Method: `GET`
- Description: Renders the home page.

### `/logout`

- Method: `GET`
- Description: Logs the user out by clearing their session data.

### `/calculator`

- Methods: `GET`, `POST`
- Description: Renders the calorie calculator page and calculates the number of steps required to burn the provided amount of calories.
- Input: `calories`

### `/calculate`

- Method: `POST`
- Description: Returns the number of steps required to burn the provided amount of calories in JSON format.
- Input: `calories`

### `/search`

- Method: `GET`
- Description: Renders the exercise search page.

### `/search_results/<body_part>/<equipment>`

- Method: `GET`
- Description: Renders the exercise search results page with exercises filtered by the provided body part and equipment.
- Input: `body_part`, `equipment`

### `/exercise_details/<exercise>`

- Method: `GET`
- Description: Renders the exercise details page for the provided exercise.
- Input: `exercise`

### `/profile`

- Method: `GET`
- Description: Renders the user's profile page with their favorite exercises.

### `/add_favorite_exercise`

- Method: `POST`
- Description: Adds the provided exercise to the user's favorites.
- Input: `exercise`

### `/remove_favorite_exercise`

- Method: `POST`
- Description: Removes the provided exercise from the user's favorites.
- Input: `exercise`
