from flask import Flask, render_template, request, url_for, redirect, make_response, jsonify
from .calCounter import Cal_Counter

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
    return render_template('search.html')


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

# TODO
def add_favorite_exercise():
    pass


# TODO
def remove_favorite_exercise():
    pass


# TODO
def get_user_favorites():
    pass
