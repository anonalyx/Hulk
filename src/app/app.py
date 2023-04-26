import psycopg2
from flask import Flask, render_template
app = Flask(__name__)

## Flask route for root URL to index() returns "index.html" using render_template
@app.route('/')
def index():
    return render_template('index.html')

## Flask route for "/db_test" connects to PostgreSQL, fetches and returns a list of tables
@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://hulk_user:sJ7uTRAXdhTsJQGOLD9Yq0uhsVBchdAE@dpg-cgrkvt1mbg5e4kh44l70-a.oregon-postgres.render.com/hulk")
    
    cur = conn.cursor()
    cur.execute("""SELECT relname FROM pg_class WHERE relkind='r'
    AND relname !~ '^(pg_|sql_)';""") # "rel" is short for relation.

    tables = [i[0] for i in cur.fetchall()] # A list() of tables.
    conn.close()
    
    return tables

    
@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgres://hulk_user:sJ7uTRAXdhTsJQGOLD9Yq0uhsVBchdAE@dpg-cgrkvt1mbg5e4kh44l70-a.oregon-postgres.render.com/hulk")
    cur = conn.cursor()
    
    response_string = ""
    directory = "models/"
    all_tables = ["account", "body_part", "equipment", "exercise", "favorite"]
    
    for table in all_tables:
        path = directory + table + ".txt"

        sql = open(path, "r")
        command = sql.read()
        sql.close()

        try:
            cur.execute(command)
            conn.commit()
            
        except:
            response_string += "Failed: "
            
        response_string += command 
        response_string += "<br><br>"
        
    conn.close()
    return response_string


@app.route('/db_insert')
def inserting():
    conn = psycopg2.connect("postgres://hulk_user:sJ7uTRAXdhTsJQGOLD9Yq0uhsVBchdAE@dpg-cgrkvt1mbg5e4kh44l70-a.oregon-postgres.render.com/hulk")
    cur = conn.cursor()
    
    response_string = ""
    directory = "models/insert_"
    all_tables = ["account", "body_part", "equipment", "exercise", "favorite"]
    
    for table in all_tables:
        path = directory + table + ".txt"

        sql = open(path, "r")
        command = sql.read()
        sql.close()

        try:
            cur.execute(command)
            conn.commit()
            
        except:
            response_string += "Failed: "
        
        response_string += command 
        response_string += "<br><br>"
        
    conn.close()
    return response_string


@app.route('/db_select')
def selecting():
    conn = psycopg2.connect("postgres://hulk_user:sJ7uTRAXdhTsJQGOLD9Yq0uhsVBchdAE@dpg-cgrkvt1mbg5e4kh44l70-a.oregon-postgres.render.com/hulk")
    cur = conn.cursor()
    
    response_string = ""
    all_tables = testing()
    
    for table in all_tables:
        command = "SELECT * FROM " + table
        cur.execute(command)
        records = cur.fetchall()
        
        response_string += table
        response_string += "<table>"

        for player in records:
            response_string += "<tr>"

            for info in player:
                response_string += "<td>{}</td>".format(info)

            response_string += "<tr>"

        response_string += "<table><br>"
    
    conn.close()
    return response_string


@app.route('/db_drop')
def dropping():
    conn = psycopg2.connect("postgres://hulk_user:sJ7uTRAXdhTsJQGOLD9Yq0uhsVBchdAE@dpg-cgrkvt1mbg5e4kh44l70-a.oregon-postgres.render.com/hulk")
    cur = conn.cursor()
    
    response_string = ""
    all_tables = ["favorite", "exercise", "account", "body_part", "equipment"]
    
    for table in all_tables:
        command = "DROP TABLE IF EXISTS " + table + ";"
        
        try:
            cur.execute(command)
            conn.commit()
        
        except:
            response_string += "Failed: "
            
        response_string += command
        response_string += "<br><br>"
        
    conn.close()
    return response_string


@app.route('/exercise_details/<exercise_id>')
def get_page_exercise_details(exercise_id):
    conn = psycopg2.connect("postgres://hulk_user:sJ7uTRAXdhTsJQGOLD9Yq0uhsVBchdAE@dpg-cgrkvt1mbg5e4kh44l70-a.oregon-postgres.render.com/hulk")
    c = conn.cursor()
    
    command = "SELECT * FROM exercise WHERE exercise_id = "
    command += str(exercise_id) + ";"
    c.execute(command)
    
    data = c.fetchall()
    data = data[0][1:]
    body_part = data[2]
    
    command = "SELECT calories FROM body_part WHERE part_name = '"
    command += body_part + "';"
    c.execute(command)
    
    calories = c.fetchall()
    calories = calories[0]
    data += calories
    
    details = {
        'exercise_name': data[0],
        'exercise_description': data[1],
        'body_part_name': data[2],
        'equipment_name': data[3],
        'calories': data[4],
    }
    
    conn.close()
    return details


def get_page_exercise_search(part_name, equipment_name, user_id = None):
    if len(part_name) == 0:
        return []
    
    conn = psycopg2.connect("postgres://hulk_user:sJ7uTRAXdhTsJQGOLD9Yq0uhsVBchdAE@dpg-cgrkvt1mbg5e4kh44l70-a.oregon-postgres.render.com/hulk")
    c = conn.cursor()
    
    command = """
    SELECT *
    FROM exercise
    WHERE (exercise_body_part = '"""
    
    for body in part_name[:-1]:
        command += body + "' OR exercise_body_part = '"
    
    if len(equipment_name) == 0:
        command += part_name[-1] + "');"
        
    else:
        command += part_name[-1] + "') AND (exercise_equipment = '"

        for equip in equipment_name[:-1]:
            command += equip + "' OR exercise_equipment = '"

        command += equipment_name[-1] + "');"
    
    c.execute(command)
    exercises = c.fetchall()
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
        conn.close()
        return search_results
    
    command = "SELECT username FROM account WHERE account_id = "
    command += str(user_id) + ";"
    
    c.execute(command)
    user = c.fetchall()
    
    if len(user) == 0:
        return "User Not Found"
    
    user = user[0][0]
    
    for result in search_results:
        command = "SELECT favorite_id FROM favorite WHERE favorite_user = '"
        command += user + "' AND favorite_exercise = '"
        command += result['exercise_name'] + "';"
        
        c.execute(command)
        favs_found = c.fetchall()
        
        if len(favs_found) == 0:
            result['favorite'] = False
            
        else:
            result['favorite'] = True
            
    conn.close()
    return search_results


@app.route('/exercise_details/<test_part>/<test_equipment>')
@app.route('/exercise_details/<test_part>/<test_equipment>/<user_id>')
def test_page_exercise_search(test_part, test_equipment, user_id = None):
    part_name = []
    equipment_name = []
    
    if test_part != 'Empty':
        part_name = ['Arms', 'Back', 'Legs', 'Cardio']
        
    if test_equipment != 'Empty':
        equipment_name = ['Dumbells', 'None']
        
    return get_page_exercise_search(part_name, equipment_name, user_id)
        

@app.route('/register/<username>/<email>')
def register_user(username, email):
    conn = psycopg2.connect("postgres://hulk_user:sJ7uTRAXdhTsJQGOLD9Yq0uhsVBchdAE@dpg-cgrkvt1mbg5e4kh44l70-a.oregon-postgres.render.com/hulk")
    c = conn.cursor()
    
    command = "SELECT * FROM account WHERE username = '"
    command += username + "' OR email = '"
    command += email + "';"
    
    c.execute(command)
    existing_user = c.fetchall()
    
    if len(existing_user) != 0:
        conn.close()
        return "Username or Email already in use"
    
    try:
        command = "SELECT account_id FROM account;"
        c.execute(command)

        curr_id = 0
        every_id = c.fetchall()

        for index in every_id:
            index_id = index[0]

            if index_id >= curr_id:
                curr_id = index_id + 1
                
        curr_id = str(curr_id)
        command = "INSERT INTO account Values ("
        command += curr_id + ", '"
        command += username + "', '"
        command += email + "');"
    
        c.execute(command)
        conn.commit()
        conn.close()
        
        registration = "Successfully Registrated <br>User ID: "
        registration += curr_id + "<br>Username: "
        registration += username + "<br>Email Address: "
        registration += email
        
        return registration
        
    except:
        conn.close()
        return "Registration Failed"

    
@app.route('/login/<username>/<email>')
def get_page_login(username, email):
    conn = psycopg2.connect("postgres://hulk_user:sJ7uTRAXdhTsJQGOLD9Yq0uhsVBchdAE@dpg-cgrkvt1mbg5e4kh44l70-a.oregon-postgres.render.com/hulk")
    c = conn.cursor()
    
    command = "SELECT account_id FROM account WHERE username = '"
    command += username + "' AND email = '"
    command += email + "';"
    
    c.execute(command)
    user_id = c.fetchall()
    conn.close()
    
    try:
        user_id = user_id[0][0]
        user_id = str(user_id)
        return user_id
    
    except:
        return "Login Failed: User Not Found"

    
@app.route('/authenticate/<username>/<email>')
def authenticate(username, email):
    login = get_page_login(username, email)
    return [login.isdigit()]


@app.route('/add_favorite/<user_id>/<exercise_id>')
def add_favorite_exercise(user_id, exercise_id):
    conn = psycopg2.connect("postgres://hulk_user:sJ7uTRAXdhTsJQGOLD9Yq0uhsVBchdAE@dpg-cgrkvt1mbg5e4kh44l70-a.oregon-postgres.render.com/hulk")
    c = conn.cursor()
    
    command = "SELECT username FROM account WHERE account_id = "
    command += str(user_id) + ";"
    
    c.execute(command)
    existing_user = c.fetchall()
    
    if len(existing_user) == 0:
        conn.close()
        return "User Not Found"
    
    command = "SELECT exercise_name FROM exercise WHERE exercise_id = "
    command += str(exercise_id) + ";"
    
    c.execute(command)
    existing_exercise = c.fetchall()
    
    if len(existing_exercise) == 0:
        conn.close()
        return "Exercise Not Found"
    
    username = existing_user[0][0]
    exercise = existing_exercise[0][0]
    
    command = "SELECT * FROM favorite WHERE favorite_user = '"
    command += username + "' AND favorite_exercise = '"
    command += exercise + "';"
    
    c.execute(command)
    existing_user = c.fetchall()
    
    if len(existing_user) != 0:
        conn.close()
        return "Favorite Already Exists"
    
    try:
        command = "SELECT favorite_id FROM favorite;"
        c.execute(command)

        curr_id = 0
        every_id = c.fetchall()

        for index in every_id:
            index_id = index[0]

            if index_id >= curr_id:
                curr_id = index_id + 1
                
        curr_id = str(curr_id)
        command = "INSERT INTO favorite Values ("
        command += curr_id + ", '"
        command += username + "', '"
        command += exercise + "');"
        
        c.execute(command)
        conn.commit()
        conn.close()
        
        result = "Added New Favorite <br>Favorite ID: "
        result += curr_id + "<br>Username: "
        result += username + "<br>Exercise: "
        result += exercise
        
        return result
        
    except:
        conn.close()
        return "Failed to Add New Favorite"


@app.route('/remove_favorite/<user_id>/<exercise_id>')
def remove_favorite_exercise(user_id, exercise_id):
    conn = psycopg2.connect("postgres://hulk_user:sJ7uTRAXdhTsJQGOLD9Yq0uhsVBchdAE@dpg-cgrkvt1mbg5e4kh44l70-a.oregon-postgres.render.com/hulk")
    c = conn.cursor()
    
    command = "SELECT username FROM account WHERE account_id = "
    command += str(user_id) + ";"
    
    c.execute(command)
    existing_user = c.fetchall()
    
    if len(existing_user) == 0:
        conn.close()
        return "User Not Found"
    
    command = "SELECT exercise_name FROM exercise WHERE exercise_id = "
    command += str(exercise_id) + ";"
    
    c.execute(command)
    existing_exercise = c.fetchall()
    
    if len(existing_exercise) == 0:
        conn.close()
        return "Exercise Not Found"
    
    username = existing_user[0][0]
    exercise = existing_exercise[0][0]
    
    command = "SELECT * FROM favorite WHERE favorite_user = '"
    command += username + "' AND favorite_exercise = '"
    command += exercise + "';"
    
    c.execute(command)
    existing_favorite = c.fetchall()
    
    if len(existing_favorite) == 0:
        conn.close()
        return "Favorite Not Found"
    
    try:
        command = "DELETE FROM favorite WHERE favorite_user = '"
        command += username + "' AND favorite_exercise = '"
        command += exercise + "';"

        c.execute(command)
        conn.commit()
        conn.close()
        
        result = "Favorite Successfully Removed <br>Username: "
        result += username + "<br>Exercise: "
        result += exercise
        
        return result
        
    except:
        conn.close()
        return "Favorite Removal Failed"


@app.route('/user_favorites/<user_id>')
def get_user_favorites(user_id):
    conn = psycopg2.connect("postgres://hulk_user:sJ7uTRAXdhTsJQGOLD9Yq0uhsVBchdAE@dpg-cgrkvt1mbg5e4kh44l70-a.oregon-postgres.render.com/hulk")
    c = conn.cursor()
    
    command = "SELECT username FROM account WHERE account_id = "
    command += str(user_id) + ";"
    c.execute(command)
    
    user_name = c.fetchall()
    user_name = user_name[0][0]
    
    command = "SELECT favorite_exercise FROM favorite WHERE favorite_user = '"
    command += user_name + "';"
    c.execute(command)
    
    exercise_list = []
    fav_exercises = c.fetchall()
    fav_exercises = fav_exercises
    
    for exercise in fav_exercises:
        exercise_name = exercise[0]
        command = "SELECT exercise_id FROM exercise WHERE exercise_name = '"
        command += exercise_name + "';"
        c.execute(command)

        exercise_id = c.fetchall()
        exercise_id = exercise_id[0][0]

        command = "SELECT * FROM exercise WHERE exercise_id = "
        command += str(exercise_id) + ";"
        
        c.execute(command)
        data = c.fetchall()
        
        for exercise in data:
            details = {
                'exercise_id': exercise[0],
                'exercise_name': exercise[1],
                'part_name': exercise[3],
                'equipment_name': exercise[4]
            }
            exercise_list.append(details)
    
    conn.close()
    return exercise_list
