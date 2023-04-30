import psycopg2
import os


# from flask import Flask, render_template
# app = Flask(__name__)


class DB:
    def __init__(self, isTest=False, isLocal=False):
        self.cur = None
        self.directory = os.path.dirname(os.path.abspath(__file__))
        self.isLocal = True
        self.isTest = isTest
        self.localURL = "postgres://hulk_user:sJ7uTRAXdhTsJQGOLD9Yq0uhsVBchdAE@dpg-cgrkvt1mbg5e4kh44l70-a.oregon-postgres.render.com/hulk"
        self.deployedURL = "postgres://hulk_user:sJ7uTRAXdhTsJQGOLD9Yq0uhsVBchdAE@dpg-cgrkvt1mbg5e4kh44l70-a/hulk"

        if self.isTest:
            self.tables = ["test_account", "test_body_part", "test_equipment", "test_exercise", "test_favorite"]

        else:
            self.tables = ["account", "body_part", "equipment", "exercise", "favorite"]
        self.conn = None

    def __enter__(self):
        self.conn = psycopg2.connect(self.localURL) if self.isLocal else psycopg2.connect(self.deployedURL)
        print(f'Connection successful: Test =  {self.isTest}')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print(f'Exiting connection: Test = {self.isTest}')
        if self.conn is not None:
            self.conn.close()

    ## connects to PostgreSQL, executes SQL commands from text files, and returns a string with their execution status
    def db_create_tables(self):
        with self.conn as conn:
            self.cur = conn.cursor()

            for table in self.tables:
                path = self.directory + '/' + 'create_' + table + ".txt"

                sql = open(path, "r")
                command = sql.read()
                sql.close()

                try:
                    self.cur.execute(command)
                    conn.commit()

                except Exception as e:
                    print('Exception while creating tables in db_creating()')
                    return e

    ## executes SQL INSERT commands from text files for a set of tables, and returns a string with their execution status
    def db_populate_records(self):
        with self.conn as conn:
            self.cur = conn.cursor()

            for table in self.tables:
                path = self.directory + '/insert_' + table + ".txt"

                sql = open(path, "r")
                command = sql.read()
                sql.close()

                try:
                    self.cur.execute(command)
                    self.conn.commit()

                except Exception as e:
                    print('Failed while inserting records db_populate_records()')
                    return e

    ## retrieves and formats all records for each table, and returns an HTML string containing the tables and records
    def db_select_all_tables(self):
        with self.conn as conn:
            self.cur = conn.cursor()
            path = self.directory + '/get_tables.txt'
            sql = open(path, "r")
            command = sql.read()
            sql.close()
            self.cur.execute(command)
            return self.cur.fetchall()

    def db_select_all_tables_and_records(self):
        with self.conn as conn:
            self.cur = conn.cursor()
            records = {}
            for table in self.tables:
                command = "SELECT * FROM " + table
                self.cur.execute(command)
                records[table] = self.cur.fetchall()
                '''
                response_string += table
                response_string += "<table>"

                for player in records:
                    response_string += "<tr>"

                    for info in player:
                        response_string += "<td>{}</td>".format(info)

                    response_string += "<tr>"

                response_string += "<table><br>"
                '''
            return records

    def db_select_col_from_table(self, table, col_index):
        with self.conn as conn:
            self.cur = conn.cursor()
            command = f"SELECT {col_index} FROM  {table}"
            self.cur.execute(command)
            records = [record[0] for record in self.cur.fetchall()]
        return records
    ## retrieves and formats all records for each table, and returns an HTML string containing the tables and records
    def db_drop(self):
        with self.conn as conn:
            self.cur = conn.cursor()
            for table in self.tables:
                command = "DROP TABLE IF EXISTS " + table + " CASCADE;"

                try:
                    self.cur.execute(command)
                    self.conn.commit()

                except Exception as e:
                    print(e)
                    return e

    ## retrieves exercise and body part information based on the exercise id, combines and returns the results as a json response
    # @app.route('/exercise_details/<exercise_id>')

    def db_get_page_exercise_details(self, exercise_id):
        with self.conn as conn:
            self.cur = conn.cursor()
            command = f"select * from exercise where exercise_id = {exercise_id};"
            self.cur.execute(command)

            data = self.cur.fetchall()
            data = data[0][1:]
            body_part = data[2]

            command = f"select calories from body_part where part_name = '{body_part}';"
            self.cur.execute(command)

            calories = self.cur.fetchall()
            calories = calories[0]
            data += calories

            details = {
                'exercise_name': data[0],
                'exercise_description': data[1],
                'body_part_name': data[2],
                'equipment_name': data[3],
                'calories': data[4],
            }

            return details

    ##  retrieves exercises by body part and equipment criteria, and adds a "favorite" flag for the specified user id.
    def db_get_exercise_search_results(self, part_name, equipment_name, user_id=None):
        print(part_name, equipment_name, user_id)
        with self.conn as conn:
            self.cur = conn.cursor()
            if len(part_name) == 0:
                return []

            command = f"""
                        select *
                        from exercise
                        where (exercise_body_part = '{part_name}')
                         and (exercise_equipment = '{equipment_name}');
                        """
            self.cur.execute(command)
            exercises = self.cur.fetchall()
            search_results = []

            for data in exercises:
                details = {
                    'exercise_id': data[0],
                    'exercise_name': data[1],
                    'part_name': data[3],
                    'equipment_name': data[4]
                }
                search_results.append(details)

            if user_id == None:
                return search_results

            command = "select username from account where account_id = "
            command += str(user_id) + ";"

            self.cur.execute(command)
            user = self.cur.fetchall()

            if len(user) == 0:
                return "user not found"

            user = user[0][0]

            for result in search_results:
                command = "select favorite_id from favorite where favorite_user = '"
                command += user + "' and favorite_exercise = '"
                command += result['exercise_name'] + "';"

                self.cur.execute(command)
                favs_found = self.cur.fetchall()

                if len(favs_found) == 0:
                    result['favorite'] = false

                else:
                    result['favorite'] = True

            return search_results

    ##  accepts three url parameters, sets search criteria based on two of them, and calls get_page_exercise_search with the criteria and the third parameter as an optional user id.
    # @app.route('/exercise_details/<test_part>/<test_equipment>')
    # @app.route('/exercise_details/<test_part>/<test_equipment>/<user_id>')

    # @app.route('/register/<username>/<email>')
    def db_register_user(self, username, email):
        with self.conn as conn:
            self.cur = conn.cursor()

            command = "select * from account where username = '"
            command += username + "' or email = '"
            command += email + "';"

            self.cur.execute(command)
            existing_user = self.cur.fetchall()

            if len(existing_user) != 0:
                return "username or email already in use"

            try:
                command = "select account_id from account;"
                self.cur.execute(command)

                curr_id = 0
                every_id = self.cur.fetchall()

                for index in every_id:
                    index_id = index[0]

                    if index_id >= curr_id:
                        curr_id = index_id + 1

                curr_id = str(curr_id)
                command = "insert into account values ("
                command += curr_id + ", '"
                command += username + "', '"
                command += email + "');"

                self.cur.execute(command)
                self.conn.commit()

                registration = "successfully registrated <br>user id: "
                registration += curr_id + "<br>username: "
                registration += username + "<br>email address: "
                registration += email

                return registration

            except:
                return "registration failed"

    ## log in a user by querying the account table for a matching username and email, and returns the user id if found, or a "login failed" message if not
    # @app.route('/login/<username>/<email>')
    def db_auth(self, username, email):
        with self.conn as conn:
            self.cur = conn.cursor()
            command = "select account_id from account where username = '"
            command += username + "' and email = '"
            command += email + "';"

            self.cur.execute(command)
            try:
                user_id = self.cur.fetchone()[0]
                return user_id
            except Exception as e:
                print(e)
                raise Exception('No user found')

    '''
    ## returns whether the given username and email combination exists in the database as a user, by calling another function and checking if the returned user id is a digit 
    # @app.route('/authenticate/<username>/<email>')
    def db_authenticate(username, email):
        login = get_page_login(username, email)
        return [login.isdigit()]
    '''

    #  adds a new exercise to the user's favorite list in a postgresql database.
    # @app.route('/add_favorite/<user_id>/<exercise_id>')
    def db_add_favorite_exercise(self, user_id, exercise_name):
        with self.conn as conn:
            self.cur = conn.cursor()
            command = f"select username from account where account_id = {user_id}"

            self.cur.execute(command)
            existing_user = self.cur.fetchall()

            if len(existing_user) == 0:
                self.conn.close()
                return "user not found"

            command = f"select exercise_name from exercise where exercise_name = '{exercise_name}'";

            self.cur.execute(command)
            existing_exercise = self.cur.fetchall()

            if len(existing_exercise) == 0:
                return "exercise not found"

            username = existing_user[0][0]
            exercise = existing_exercise[0][0]

            command = "select * from favorite where favorite_user = '"
            command += username + "' and favorite_exercise = '"
            command += exercise + "';"

            self.cur.execute(command)
            existing_user = self.cur.fetchall()

            if len(existing_user) != 0:
                return "favorite already exists"

            try:
                command = "select favorite_id from favorite;"
                self.cur.execute(command)

                curr_id = 0
                every_id = self.cur.fetchall()

                for index in every_id:
                    index_id = index[0]

                    if index_id >= curr_id:
                        curr_id = index_id + 1

                curr_id = str(curr_id)
                command = "insert into favorite values ("
                command += curr_id + ", '"
                command += username + "', '"
                command += exercise + "');"

                self.cur.execute(command)
                conn.commit()

                result = "added new favorite <br>favorite id: "
                result += curr_id + "<br>username: "
                result += username + "<br>exercise: "
                result += exercise

                return result

            except:
                return "failed to add new favorite"

    ## route for removing a user's favorite exercise from the database based on the user id and exercise id parameters
    # @app.route('/remove_favorite/<user_id>/<exercise_id>')
    def db_remove_favorite_exercise(self, user_id, exercise_name):
        with self.conn as conn:
            self.cur = conn.cursor()

            command = f"select username from account where account_id = {user_id};"

            self.cur.execute(command)
            existing_user = self.cur.fetchall()

            if len(existing_user) == 0:
                return "user not found"

            command = f"select exercise_name from exercise where exercise_name = '{exercise_name}';"

            self.cur.execute(command)
            existing_exercise = self.cur.fetchall()

            if len(existing_exercise) == 0:
                return "Exercise Not Found"

            username = existing_user[0][0]
            exercise = existing_exercise[0][0]

            command = "SELECT * FROM favorite WHERE favorite_user = '"
            command += username + "' AND favorite_exercise = '"
            command += exercise + "';"

            self.cur.execute(command)
            existing_favorite = self.cur.fetchall()

            if len(existing_favorite) == 0:
                return "Favorite Not Found"

            try:
                command = "DELETE FROM favorite WHERE favorite_user = '"
                command += username + "' AND favorite_exercise = '"
                command += exercise + "';"

                self.cur.execute(command)
                conn.commit()

                result = "Favorite Successfully Removed <br>Username: "
                result += username + "<br>Exercise: "
                result += exercise

                return result

            except:
                return "Favorite Removal Failed"

    # # gets the list of favorite exercises for a given user, retrieves details about the exercises from the
    # database, and returns them as a list of dictionaries @app.route('/user_favorites/<user_id>')
    def db_get_user_favorites(self, user_id):
        with self.conn as conn:
            self.cur = conn.cursor()

            command = "SELECT username FROM account WHERE account_id = "
            command += str(user_id) + ";"
            self.cur.execute(command)

            user_name = self.cur.fetchall()
            user_name = user_name[0][0]

            command = "SELECT favorite_exercise FROM favorite WHERE favorite_user = '"
            command += user_name + "';"
            self.cur.execute(command)

            exercise_list = []
            fav_exercises = self.cur.fetchall()
            fav_exercises = fav_exercises

            for exercise in fav_exercises:
                exercise_name = exercise[0]
                command = "SELECT exercise_id FROM exercise WHERE exercise_name = '"
                command += exercise_name + "';"
                self.cur.execute(command)

                exercise_id = self.cur.fetchall()
                exercise_id = exercise_id[0][0]

                command = "SELECT * FROM exercise WHERE exercise_id = "
                command += str(exercise_id) + ";"

                self.cur.execute(command)
                data = self.cur.fetchall()

                for exercise in data:
                    details = {
                        'exercise_id': exercise[0],
                        'exercise_name': exercise[1],
                        'part_name': exercise[3],
                        'equipment_name': exercise[4]
                    }
                    exercise_list.append(details)

            return exercise_list
