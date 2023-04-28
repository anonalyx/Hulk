from flask import Flask, render_template, request, url_for, redirect, make_response, jsonify
from src.app.calCounter import Cal_Counter
from src.app.models.db_routes import DB
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


# TODO
@app.route('/search', methods=['GET'])
def get_page_exercise_search():
    body_data = ["Biceps","Abdominals","Shoulders", "Back", "Quads"]
    equipment_data = ["None", "Kettle_bell", "Barbell", "Exercise_Ball", "Dumbbell"]

    data = {"body_data": body_data, "equipment_data": equipment_data}
    return render_template('search.html', data=data)



@app.route('/search_results/<body_part>/<equipment>', methods=['GET'])
def get_page_search_results(body_part, equipment):
    print(body_part, equipment)
    with DB as db:
        data = db.db_get_exercise_search_results([body_part], [equipment])

    # TODO: Remove hardcoded data when exercise_search is implemented
    #data = [{'exercise': 'Push_Up', 'body_part': body_part, 'equipment': equipment},
            # {'exercise': 'Bicep_Curl', 'body_part': body_part, 'equipment': equipment},
            # {'exercise': 'Squat', 'body_part': body_part, 'equipment': equipment},
            # {'exercise': 'Lunge', 'body_part': body_part, 'equipment': equipment}]

    #headers = {"exercise": "Exercise",
    #           "body_part": "Body Part",
    #           "equipment": "Equipment"}
    
    ids = {'buttons': 'favorites-button', }


    return render_template('search_results.html', data=data, headers=headers)

@app.route('/profile', methods=['GET'])
def get_page_profile():
    with DB as db:
        data = db.db_get_user_favorites(user_id)

    user_data = {'username': 'sample', 'email': 'sample@gmail.com'}

    data = [{'exercise': 'Push_Up', 'body_part': 'Chest', 'equipment': 'None'},
            {'exercise': 'Bicep_Curl', 'body_part': 'Biceps', 'equipment': 'Dumbbell'},
            {'exercise': 'Squat', 'body_part': 'Quads', 'equipment': 'Barbell'},
            {'exercise': 'Lunge', 'body_part': 'Quads', 'equipment': 'None'}]
    
    headers = {"exercise": "Exercise",
               "body_part": "Body Part",
               "equipment": "Equipment"}
    
    return render_template('profile.html', data=data, user_data=user_data, headers=headers)

# TODO
@app.route('/signup', methods=['POST'])
def register_user(username, email):
    with DB as db:
        db.db_register_user(username, email)
    return redirect(url_for('home'))


# TODO
@app.route('/', methods=['GET'])
def get_page_login():
    return render_template('login.html')


# TODO
@app.route('/auth', methods=['POST'])
def authenticate(username,email):
    with DB as db:
        db.db_auth(username, email)
    return redirect(url_for('home'))


@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

# TODO
@app.route('/add_favorite/<user_id>/<exercise_id')
def add_favorite_exercise(user_id, exercise_id):
    with DB as db:
        db.db_add_favorite_exercise(user_id, exercise_id)



# TODO
@app.route('/remove_favorite/<user_id>/<exercise_id>')
def remove_favorite_exercise(user_id, exercise_id):
    with DB as db:
        db.db_remove_favorite_exercise(user_id, exercise_id)
    pass


# TODO
def get_user_favorites():
    pass
