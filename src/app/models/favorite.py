'''CREATE TABLE IF NOT EXISTS favorite (
favorite_id INT GENERATED ALWAYS AS IDENTITY,
favorite_user VARCHAR(15),
favorite_exercise VARCHAR(30),
CONSTRAINT fk_user FOREIGN KEY(favorite_user) REFERENCES account(username),
CONSTRAINT fk_exercise FOREIGN KEY(favorite_exercise) REFERENCES exercise(exercise_name));'''
