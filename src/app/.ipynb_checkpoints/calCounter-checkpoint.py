from sympy import symbols, Eq, solve
import re

class Cal_Counter:
    def __init__(self):
        #self.a = 0.109166
        #self.b = 41867.305254
        
        with open("fitbase_data/RunForestRun.txt") as parameters_file:
            parameters = parameters_file.read()
        
        pattern = re.compile(r"(-?\d+(.\d+)?)\n(-?\d+(.\d+)?)")
        match = pattern.search(parameters)

        if match:
            self.a = float(match.group(1))
            self.b = float(match.group(3))
            
        else:
            self.a = None
            self.b = None
    
    def getSteps(self, goal):
        x = symbols('x')
        y = goal

        equation = Eq(self.a * x + self.b, y)
        sol = solve(equation)[0]

        if sol < 0:
            return 0

        else:
            return int(sol)
        
    def getCalories(self, reps, exercise = None, bodyPart = None):
        if exercise == 'Running' or bodyPart == 'Cardio':
            beta0, beta1 = self.b, self.a
            return beta0 + beta1 * reps

        elif exercise == 'Bicep Curl' or bodyPart == 'Arms':
            return 2 * reps

        elif exercise == 'Rows' or bodyPart == 'Back':
            return 3/2 * reps

        elif exercise == 'Squats' or bodyPart == 'Legs':
            return 5/2 * reps

        elif exercise == 'Sit-Ups' or bodyPart == 'Abs':
            return 3/5 * reps

        else:
            return 0
    
    def getRepititions(self, calories, exercise = None, bodyPart = None):
        if exercise == 'Running' or bodyPart == 'Cardio':
            return getSteps(calories)

        elif exercise == 'Bicep Curl' or bodyPart == 'Arms':
            return 1/2 * calories

        elif exercise == 'Rows' or bodyPart == 'Back':
            return 2/3 * calories

        elif exercise == 'Squats' or bodyPart == 'Legs':
            return 2/5 * calories

        elif exercise == 'Sit-Ups' or bodyPart == 'Abs':
            return 5/3 * calories

        else:
            return 0
        
'''
testing = Cal_Counter()
print(testing.a)
print(testing.b)
'''
