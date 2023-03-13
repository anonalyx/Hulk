from flask import Flask, render_template, request, url_for, redirect
from calCounter import Cal_Counter

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

