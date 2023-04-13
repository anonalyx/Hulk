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
    try:
        args = sys.argv
        goal = eval(args[1])
        
        if goal < 0:
            raise Exception()
            
        else:
            return goal

    except:
        return 0
    
def takeSample(data, columns):
    sample_size = 10000
    
    data_sample = data[columns].sample(
        n = sample_size, replace = True
    )
    
    data_sample = data_sample.groupby(columns[0])
    data_sample = data_sample.sum()

    return data_sample
    
fit = pd.read_csv('dailyActivity_merged.csv')

columns = ['Id', 'TotalSteps', 'Calories']
train_data = takeSample(fit, columns)

model = smf.ols(
    formula = 'Calories ~ TotalSteps', 
    data = train_data
).fit()

calories = getInput()
stepSim = calCalc(calories)
print(stepSim, 'steps to burn', calories, 'calories')
