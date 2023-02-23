import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from sympy import symbols, Eq, solve

# Function to get output
def calCalc(calories):
    try:
        distance = target(calories, model)
        return int(distance)
    
    except:
        return 0

def target(goal, model):
    beta0, beta1 = model.params
    
    x = symbols('x')
    y = goal

    equation = Eq(beta0 + beta1 * x, y)
    sol = solve(equation)[0]
    
    if sol < 0:
        return 0

    else:
        return sol
    
def getInput():
    args = sys.argv
    
    try:
        goal = eval(args[1])
        
        if goal < 0:
            raise Exception()
            
        else:
            return goal

    except:
        return 0
    
fit = pd.read_csv('Fitabase Data 4.12.16-5.12.16/dailyActivity_merged.csv')

stats = fit.groupby(['Id'])
stats = stats.sum(numeric_only = True)

model = smf.ols(
    formula = 'Calories ~ TotalSteps', 
    data = stats
).fit()

'''
calories = getInput()
stepSim = calCalc(calories)
print(stepSim, 'steps to burn', sys.argv[1], 'calories')
'''
