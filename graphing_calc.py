import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # This tells it to save files without opening a window
import numpy as np
import sympy as simp
from sympy import symbols, solve
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
import os
import json


class claculator_type:




    def __init__(self):


        self.filename = "calculator_history.json"
        self.history_list = self.load_history()


    def load_history(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return {}


    def save_to_json(self, problem, solution):
        # Convert solution to string so JSON can handle it (Sympy objects won't save directly)
        self.history_list[problem] = str(solution)
        with open(self.filename, 'w') as f:
            json.dump(self.history_list, f, indent=4)




class arithmetic(claculator_type):


    def __init__(self):


        super().__init__()


    def mathematics(self, user_input):  #should allow +,-, / , *, **, roots,


        # 1. Take the input in mainloop
        # 2. Use eval() or simp.sympify() to solve it
        solution = simp.sympify(user_input)
        print(solution)
        self.save_to_json(user_input, solution)






class expresions(claculator_type):


    def __init__(self):


        super().__init__()


    def expressions(self, user_input):    #should allow things like sovle for x: 3x=7 or 4x-2=0 but only with one x variable.
        # 1. Define x as a symbol
        x = symbols('x')


        # 2. Handle the equals sign
        # Sympy solve() works best if the equation equals 0.
        # So "3*x = 6" becomes "3*x - 6"
        if "=" in user_input:
            left, right = user_input.split("=")
            # Use parse_expr to allow for implicit multiplication like '3x'
            transformations = (standard_transformations + (implicit_multiplication_application,))
            equation = parse_expr(left, transformations=transformations) - parse_expr(right, transformations=transformations)
        else:
            equation = parse_expr(user_input)


        # 3. Solve for x
        solution = solve(equation, x)


        print(f"x = {solution}")


        self.save_to_json(user_input, solution)








class graphing(claculator_type): #should graph the functions the user inputed.


    def __init__(self):


        super().__init__()




    def graph(self, user_input):


        plt.clf()
        fig, ax = plt.subplots()






        x = symbols('x')




        #parse
        transformations = (standard_transformations + (implicit_multiplication_application,))
        expr = parse_expr(user_input, transformations=transformations)




        f = simp.lambdify(x, expr, 'numpy')
        xpoints = np.linspace(-20, 20, 400)
        ypoints = f(xpoints)




        # 5. LOCK THE GRID (This is what you need)
        plt.xlim(-20, 20) # Locks horizontal
        plt.ylim(-20, 20) # Locks vertical






        #looks


        plt.xlabel("X-Axis")
        plt.ylabel("Y-Axis")
        plt.axhline(0, color='black', linewidth=1) # The X axis line
        plt.axvline(0, color='black', linewidth=1) # The Y axis line
        plt.grid(True, linestyle=':', alpha=0.6)






        plt.plot(xpoints, ypoints, linestyle = 'dashed')


        plt.savefig('temporary_graph.png')    #should save as temp png that user can delete later to graph a new thing


        print("success check your files user.")


















#main loop / console ui


calc_math = arithmetic()
calc_expr = expresions()
calc_graph = graphing()


def start_calclator():
    print(" a. arithmetic. ")
    print(" b. expresions. ")
    print(" c. graph. ")
    print(" d. show previous result. ")
    print(" e. show history. ")
    print(" f. delete temp graph, to make a new one! ")
    print(" g. leave. ")




def delete_png():


    if os.path.exists('temporary_graph.png'):
        os.remove('temporary_graph.png')
        print(' graph removed! :) ')
    else:
        print('graph does not yet exist')




while True:
    start_calclator()
    user_choice = input("Pick an option: ")


    if user_choice == "a":
        problem = input("Enter your math problem: ")
        calc_math.mathematics(problem) # This "sends" the problem to the class


    elif user_choice == "b":
        expresion = input("Enter your expresion: ") #vaild input should be things like 3x = 6
        calc_expr.expressions(expresion)


    elif user_choice == "c":
        function = input("Enter your function to graph: ")
        calc_graph.graph(function)


    elif user_choice == "d":      # should only print Previous result for ethier expresions or arithmetic no remakeing the matplotlib graph file
        history = calc_math.load_history() # Pull fresh from file
        if history:
            # Get the last key/value added to the dictionary
            last_problem = list(history.keys())[-1]
            last_result = history[last_problem]
            print(f"Previous Problem: {last_problem}")
            print(f"Previous Result: {last_result}")
        else:
            print("No history found.")


    elif user_choice == "e":
        history = calc_math.load_history()
        print("--- Calculation History ---")
        for prob, res in history.items():
            print(f"{prob} = {res}")
        print("---------------------------")


    elif user_choice == "f":
        delete_png()


    elif user_choice == "g":
        print(" Thank You For Using This Calculator :) ")
        break