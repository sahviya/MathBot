import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define the variable
x = sp.symbols('x')

# Define the equation
equation = sp.Eq(2*x**2 + 5 - 3, 8)

# Solve the equation
solutions = sp.solve(equation, x)
print(solutions)

# 1. Basic Arithmetic Operations
def basic_operations():
    print("\nBasic ArithmetiAc Operations:")
    while True:
        user_input = input("Enter a mathematical expression or 'exit' to quit: ").strip()

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        try:
            result = sp.sympify(user_input)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}. Please enter a valid expression.")

# 2. Solving Algebraic Equations (e.g., Linear, Quadratic)
def solve_equations():
    print("\nSolving Equations:")
    while True:
        equation_input = input("Enter an equation (e.g., 2*x + 3 = 0) or 'exit': ").strip()

        if equation_input.lower() == 'exit':
            print("Exiting equation solver.")
            break

        try:
            # Splitting the equation into left and right parts
            lhs, rhs = equation_input.split('=')
            lhs, rhs = sp.sympify(lhs), sp.sympify(rhs)
            equation = sp.Eq(lhs, rhs)

            # Solve the equation
            solutions = sp.solve(equation)
            print(f"Solutions: {solutions}")
        except Exception as e:
            print(f"Error: {e}. Please enter a valid equation.")
    
 #3. solving trignometric operations
def trigonometric_operations():
    print("\nTrigonometric Operations:")
    while True:
        trig_input = input("Enter a trigonometric expression (e.g., sin(pi/2), cos(0)) or 'exit': ").strip()

        if trig_input.lower() == 'exit':
            print("Exiting trigonometric operations.")
            break

        try:
            result = sp.sympify(trig_input)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}. Please enter a valid expression.")

# 4. Plotting Graphs 
def plot_graph():
    print("\nGraph Plotter:")
    while True:
        function_input = input("Enter a mathematical function (e.g., x**2, sin(x), or 'exit'): ").strip()

        if function_input.lower() == 'exit':
            print("Exiting graph plotter.")
            break

        try:
            # Create a lambda function to evaluate
            function = sp.lambdify('x', sp.sympify(function_input), 'numpy')
            x_vals = np.linspace(-10, 10, 400)
            y_vals = function(x_vals)

            # Plotting the graph
            plt.plot(x_vals, y_vals)
            plt.title(f"Graph of {function_input}")
            plt.xlabel("x")
            plt.ylabel("f(x)")
            plt.grid(True)
            plt.show()
        except Exception as e:
            print(f"Error: {e}. Please enter a valid function.")

#5. Derivative Calculation
def calculate_derivative():
    print("\nDerivative Calculator:")
    while True:
        func_input = input("Enter a function to differentiate (e.g., x**2 + 3*x or 'exit'): ").strip()

        if func_input.lower() == 'exit':
            print("Exiting derivative calculator.")
            break

        try:
            x = sp.symbols('x')
            func = sp.sympify(func_input)
            derivative = sp.diff(func, x)
            print(f"Derivative: {derivative}")
        except Exception as e:
            print(f"Error: {e}. Please enter a valid function.")

#6. Integral Calculation
def calculate_integral():
    print("\nIntegral Calculator:")
    while True:
        func_input = input("Enter a function to integrate (e.g., x**2 + 3*x or 'exit'): ").strip()

        if func_input.lower() == 'exit':
            print("Exiting integral calculator.")
            break

        try:
            x = sp.symbols('x')
            func = sp.sympify(func_input)

            # Indefinite Integral
            indefinite_integral = sp.integrate(func, x)
            print(f"Indefinite Integral: {indefinite_integral}")

            # Definite Integral (from 0 to 1 as an example)
            definite_integral = sp.integrate(func, (x, 0, 1))
            print(f"Definite Integral (from 0 to 1): {definite_integral}")
        except Exception as e:
            print(f"Error: {e}. Please enter a valid function.")

#7. Limit Calculation
def calculate_limit():
    print("\nLimit Calculator:")
    while True:
        func_input = input("Enter a function to find the limit (e.g., x**2 - 1)/(x - 1 or 'exit'): ").strip()

        if func_input.lower() == 'exit':
            print("Exiting limit calculator.")
            break

        try:
            x = sp.symbols('x')
            func = sp.sympify(func_input)

            # Limit as x approaches 1 (as an example)
            limit = sp.limit(func, x, 1)
            print(f"Limit as x approaches 1: {limit}")
        except Exception as e:
            print(f"Error: {e}. Please enter a valid function.")

# 8. Main Menu and User Interaction
def main():
    while True:
        print("\nWelcome to the Math Solver Bot!")
        print("1. Basic Arithmetic Operations")
        print("2. Solve Algebraic Equations")
        print("3. Trigonometric Operations")
        print("4. Plot Graph")
        print("5. Derivative Calculator")
        print("6. Integral Calculator")
        print("7. Limit Calculator")
        print("8. Exit")

        choice = input("Enter your choice (1-9): ").strip()

        if choice == '1':
            basic_operations()
        elif choice == '2':
            solve_equations()
        elif choice == '3':
            trigonometric_operations()
        elif choice == '4':
            plot_graph()
        elif choice == '5':
            calculate_derivative()
        elif choice == '6':
            calculate_integral()
        elif choice == '7':
            calculate_limit()
        elif choice == '8':
            print("Exiting the Math Solver Bot. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "_main_":
    main()