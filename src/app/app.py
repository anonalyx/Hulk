from flask import Flask, render_template, request, url_for, redirect, make_response, jsonify, session
from calCounter import Cal_Counter
import os

app = Flask(__name__)

# commenting this out. Writing index route.
'''
@app.route('/')
def index():
    return redirect(url_for('calculator'))  # Temporarily redirecting to calorie calculator
'''


@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    if request.method == 'GET':
        return render_template('calculator.html')
    if request.method == 'POST':
        calories = request.form['calories']
        counter = Cal_Counter()
        steps = counter.getSteps(calories)
        calcResult = (calories, steps)
        return render_template('calculator.html', result=calcResult)


@app.route('/calculate', methods=['POST'])
def calculate():
    req = request.get_json()

    counter = Cal_Counter()
    steps = counter.getSteps(int(req['calories']))

    response = make_response(jsonify({'steps': steps}), 200)

    return response


'''
ROUTES:
    Pages
    - Login
    - Landing Page
    - Exercise Search
    - Exercise Result
    - Profile

'''


# TODO
def get_page_exercise_details():
    pass



@app.route('/search', methods=['GET'])
def get_page_exercise_search():

    #body_data =  get_column("body_part", "name")
    #equip_data = get_column("equipment", "name"")

    # TODO: Remove hardcoded data when get_column is implemented
    body_data = ["Biceps","Abdominals","Shoulders", "Back", "Quads"]
    equipment_data = ["None", "Kettle_bell", "Barbell", "Exercise_Ball", "Dumbbell"]

    data = {"body_data": body_data, "equipment_data": equipment_data}

    return render_template('search.html', data=data)


@app.route('/search_results/<body_part>/<equipment>', methods=['GET'])
def get_page_exercise_search_results(body_part, equipment):

    #data = exercise_search('body_part', 'equipment')

    # TODO: Remove hardcoded data when exercise_search is implemented
    data = [{'exercise': 'Push_Up', 'body_part': body_part, 'equipment': equipment},
            {'exercise': 'Bicep_Curl', 'body_part': body_part, 'equipment': equipment},
            {'exercise': 'Squat', 'body_part': body_part, 'equipment': equipment},
            {'exercise': 'Lunge', 'body_part': body_part, 'equipment': equipment}]

    headers = {"exercise": "Exercise",
               "body_part": "Body Part",
               "equipment": "Equipment"}

    svg_path = os.path.join(app.static_folder, 'icons', 'favorites_icon.svg')
    svg_content = read_svg_content(svg_path)

    return render_template('search_results.html', data=data, headers=headers, svg_content=svg_content)

# TODO
@app.route('/signup', methods=['POST'])
def register_user():
    return redirect(url_for('home'))


# TODO
@app.route('/', methods=['GET'])
def get_page_login():
    return render_template('login.html')


# TODO
@app.route('/auth', methods=['POST'])
def authenticate():
    return redirect(url_for('home'))


@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/add_favorite_exercise', methods=['POST'])
def add_favorite_exercise():
    """ Adds an exercise to the user's favorites """
    if 'user' in session:
        user_id = session['user']
        exercise = request.form.get('exercise')
        # db_add_favorite_exercise(exercise, user_id)
        return {'success': True,
                'message': 'Favorite added'}
    else:
        return {'success': False,
                'message': 'Please log in or create an account to add favorites'}

# TODO
@app.route('/remove_favorite_exercise', methods=['POST'])
def remove_favorite_exercise():
    """ Removes an exercise from the user's favorites """
    if 'user' in session:
        user_id = session['user']
        exercise = request.form.get('exercise')
        # db_remove_favorite_exercise(exercise, user_id)
        return {'success': True,
                'message': 'Favorite removed'}
    else:
        return {'success': False,
                'message': 'Please log in or create an account to remove favorites'}


# TODO
def get_user_favorites():
    pass

# TODO
def get_column(table, column):
    """
    Description: Get specified columns from a table

    Parameters:
        table: String - table name
        columns: String - column name

    Returns: list of strings - column values
    """
    pass

def read_svg_content(filename):
    with open(filename, 'r') as f:
        content = f.read()
    return content
