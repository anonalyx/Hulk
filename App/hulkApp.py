from flask import Flask, render_template, request, url_for, redirect
#from Hulk import calCalc

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
        steps = calculator(calories) # This will be replaced by calCalc function
        calcResult = (calories, steps)
        return render_template('calculator.html', result=calcResult)

def calculator(calories):
    return int(calories) * 2 + 50
