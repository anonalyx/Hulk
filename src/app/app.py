from flask import Flask, render_template, request, url_for, redirect, make_response, jsonify, session
from src.app.calCounter import Cal_Counter
from src.app.models.db_routes import DB
from functools import wraps

app = Flask(__name__)
app.secret_key = 'OurSecret'

# commenting this out. Writing index route.
'''
@app.route('/')
def index():
    return redirect(url_for('calculator'))  # Temporarily redirecting to calorie calculator
'''


def login_required(f):
    print('redirecting to login page')
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('get_page_login'))
        return f(*args, **kwargs)
    return decorated_function

with DB() as db:
    db.db_drop()
    db.db_create_tables()
    db.db_populate_records()



@app.route('/calculator', methods=['GET', 'POST'])
@login_required
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
@login_required
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
@app.route('/exercise_details/<exercise>', methods=['GET'])
@login_required
def get_page_exercise_details(exercise):
    try:
        with DB() as db:
            data = db.db_get_page_exercise_details(exercise)
    except Exception as e:
        print(f'Error: {e}')
        return

    return render_template('exercise_details.html', data=data)


# TODO
@app.route('/search', methods=['GET'])
@login_required
def get_search():
    with DB() as db:
        body_data = db.db_select_col_from_table('body_part', 'part_name')
        equipment_data = db.db_select_col_from_table('equipment','equipment_name')

    data = {"body_data": body_data, "equipment_data": equipment_data}
    return render_template('search.html', data=data)



@app.route('/search_results/<body_part>/<equipment>', methods=['GET'])
@login_required
def get_page_search_results(body_part, equipment):
    print(body_part, equipment)
    try:
        with DB() as db:
            print(db)
            print(dir(db))
            data = db.db_get_exercise_search_results(body_part, equipment)
    except Exception as e:
        print(f'Error: {e}')
        return

    # TODO: Remove hardcoded data when exercise_search is implemented
    #data = [{'exercise': 'Push_Up', 'body_part': body_part, 'equipment': equipment},
            # {'exercise': 'Bicep_Curl', 'body_part': body_part, 'equipment': equipment},
            # {'exercise': 'Squat', 'body_part': body_part, 'equipment': equipment},
            # {'exercise': 'Lunge', 'body_part': body_part, 'equipment': equipment}]

    headers = {"exercise": "Exercise",
              "body_part": "Body Part",
              "equipment": "Equipment"}

    return render_template('search_results.html', data=data, headers=headers)

@app.route('/profile', methods=['GET'])
@login_required
def get_page_profile():
    try:
        with DB() as db:
            data = db.db_get_user_favorites(session['user_id'])

        headers = {"exercise": "Exercise",
                   "body_part": "Body Part",
                   "equipment": "Equipment"}
    except Exception as e:
        print('Get page profile failed')
        return e


    return render_template('profile.html', data=data, headers=headers)

# TODO
@app.route('/signup', methods=['POST'])
def register_user(username= None, email=None):
    if username is None or email is None:
        username = request.form['username']
        email = request.form['email']

    try:
        with DB() as db:
            db.db_register_user(username, email)
            session['user_id'] = db.db_auth(username, email)
        session['username'] = username
        session['email'] = email
        return redirect(url_for('home'))
    except Exception as e:
        print(e)
        return redirect(url_for('get_page_login'))


# TODO
@app.route('/', methods=['GET'])
def get_page_login():
    return render_template('login.html')


# TODO
@app.route('/auth', methods=['POST'])
def authenticate():
    username = request.form['username']
    email = request.form['email']
    try:
        with DB() as db:
            session['user_id'] = db.db_auth(username, email)
            session['email'] = email
            print(f"user session id is {session['user_id']}")
        return redirect(url_for('home'))
    except Exception as e:
        print(e)
        return redirect(url_for('get_page_login'))


@app.route('/home', methods=['GET'])
@login_required
def home():
    return render_template('home.html')

# TODO
@app.route('/add_favorite_exercise', methods=['POST'])
@login_required
def add_favorite_exercise():
    print('adding favorite exercise')
    print(request.form)
    """ Adds an exercise to the user's favorites """
    if 'user_id' in session:
        print('user is in session')
        user_id = session['user_id']
        exercise = request.form.get('exercise')
        print(user_id, exercise)
        with DB() as db:
            print(db.conn)
            db.db_add_favorite_exercise( user_id, exercise)
        return {'success': True,
                'message': 'Favorite added'}
    else:
        return {'success': False,
                'message': 'Please log in or create an account to add favorites'}

# TODO
@app.route('/remove_favorite_exercise', methods=['POST'])
@login_required
def remove_favorite_exercise():
    print('removing favorite exercise')
    """ Removes an exercise from the user's favorites """
    print(session)
    print(request.form)
    if 'user_id' in session:
        user_id = session['user_id']
        exercise = request.form.get('exercise')
        print(f'exercise selected {exercise}')
        with DB() as db:
            db.db_remove_favorite_exercise(user_id, exercise)
        return {'success': True,
                'message': 'Favorite removed'}
    else:
        return {'success': False,
                'message': 'Please log in or create an account to remove favorites'}
# TODO
def get_user_favorites():
    pass
