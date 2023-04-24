from sympy import symbols, Eq, solve

class Cal_Counter:
    def __init__(self):
        self.a = 0.109166
        self.b = 41867.305254
    
    def getSteps(self, goal):
        x = symbols('x')
        y = goal

        equation = Eq(self.a * x + self.b, y)
        sol = solve(equation)[0]

        if sol < 0:
            return 0

        else:
            return int(sol)