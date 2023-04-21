from flask import Flask, render_template, request, url_for, redirect, make_response, jsonify
from .calCounter import Cal_Counter

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('calculator')) # Temporarily redirecting to calorie calculator

@app.route('/calculator', methods=['GET','POST'])
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
#TODO
def get_page_exercise_details():
    pass

#TODO
def get_page_exercise_search():
    pass

#TODO
def register_user():
    pass

#TODO
def get_page_login():
    pass

#TODO
def authenticate():
    pass

#TODO
def add_favorite_exercise():
    pass

#TODO
def remove_favorite_exercise():
    pass

#TODO
def get_user_favorites():
    pass
