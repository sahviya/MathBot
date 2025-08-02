from flask import Flask, render_template, request, jsonify
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import io
import base64
from sympy import symbols, Eq, solve

app = Flask(__name__)

# 1. Basic Arithmetic Operations
def basic_operations(expression):
    try:
        result = sp.sympify(expression)
        return str(result)
    except Exception as e:
        return f"Error: {e}"

# 2. Solve Algebraic Equations
def solve_equations(equation):
    try:
        lhs, rhs = equation.split('=')
        lhs, rhs = sp.sympify(lhs), sp.sympify(rhs)
        equation = sp.Eq(lhs, rhs)
        solutions = sp.solve(equation)
        return str(solutions)
    except Exception as e:
        return f"Error: {e}"

#3. trignometric operations
def trigonometric_operations(expression):
    """
    Solves trigonometric expressions with both numeric and symbolic variables.
    - Returns symbolic derivatives for trigonometric functions.
    - Returns exact results for numeric trigonometric expressions.

    Args:
        expression: The trigonometric expression to solve.

    Returns:
        The result of the trigonometric operation (either symbolic or exact).
    """
    try:
        # Define the symbol 'x' for symbolic calculations
        x = sp.symbols('x')

        # Parse the input expression using sympy's sympify
        expr = sp.sympify(expression)

        # If the expression is symbolic (e.g., sin(x)), we compute its derivative
        if isinstance(expr, sp.Basic):
            # Calculate the symbolic derivative
            if expr.has(x):  # Ensure we have 'x' in the expression
                derivative = sp.diff(expr, x)
                return f"Derivative of {expression}: {derivative}"

            # If it's a number (like sin(30)), evaluate it exactly
            if isinstance(expr, sp.Number):
                return f"Result: {expr}"

        # For exact numeric evaluation (like sin(30) in degrees), we return exact fractions
        if isinstance(expr, sp.Basic) and any(isinstance(arg, sp.Number) for arg in expr.args):
            # Convert degrees to radians if the argument is numeric
            for i, arg in enumerate(expr.args):
                if isinstance(arg, sp.Number):
                    expr = expr.subs(arg, arg * sp.pi / 180)  # Convert degrees to radians

            result = expr.evalf()  # Evaluate to exact result, avoiding decimal approximation
            return f"Exact Result: {expr}"

        return f"Expression: {expr}"

    except Exception as e:
        return f"Error: {e}"

# 4. Plot Graph
def plot_graph(function):
    try:
        # Convert the function to a callable
        x = sp.symbols('x')
        func = sp.lambdify(x, sp.sympify(function), 'numpy')

        # Generate x and y values
        x_vals = np.linspace(-10, 10, 400)
        y_vals = func(x_vals)

        # Plotting the graph
        plt.figure(figsize=(5, 5))
        plt.plot(x_vals, y_vals)
        plt.title(f"Graph of {function}")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid(True)

        # Save the plot to a PNG image in memory
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)

        # Encode the image as Base64
        img_b64 = base64.b64encode(img.read()).decode('utf-8')
        return img_b64
    except Exception as e:
        return f"Error: {e}"
    
# 5. Derivative Calculation
def calculate_derivative(function):
    try:
        x = sp.symbols('x')
        func = sp.sympify(function)
        derivative = sp.diff(func, x)
        return str(derivative)
    except Exception as e:
        return f"Error: {e}"

# 6. Integral Calculation
def calculate_integral(function):
    try:
        x = sp.symbols('x')
        func = sp.sympify(function)
        indefinite_integral = sp.integrate(func, x)
        definite_integral = sp.integrate(func, (x, 0, 1))
        return str(indefinite_integral), str(definite_integral)
    except Exception as e:
        return f"Error: {e}"

# 7. Limit Calculation
def calculate_limit(function):
    try:
        x = sp.symbols('x')
        func = sp.sympify(function)
        limit = sp.limit(func, x, 1)
        return str(limit)
    except Exception as e:
        return f"Error: {e}"


# Flask Routes
# Route for Welcome Page (wlc.html)
@app.route('/')
def welcome():
    return render_template('wlc.html')

# Route for Math Solver Bot Page (mathbot.html)
@app.route('/index')
def index():
    return render_template('index.html')  


@app.route('/basic_operations', methods=['POST'])
def basic_operations_route():
    expression = request.form.get('expression')
    result = basic_operations(expression)
    return jsonify(result=result)

@app.route('/solve_equations', methods=['POST'])
def solve_equations_route():
    equation = request.form.get('equation')
    result = solve_equations(equation)
    return jsonify(result=result)

@app.route('/trigonometric', methods=['POST'])
def handle_trigonometric_operations():
    """
    This route handles POST requests to the '/trigonometric' endpoint.
    It receives a JSON payload containing the trigonometric expression 
    and returns the calculated result as JSON.
    """
    data = request.get_json()
    expression = data.get('function', '')  # Change 'function' to 'expression'

    if not expression:
        return jsonify({'error': 'No expression provided'}), 400

    result = trigonometric_operations(expression)
    return jsonify({'result': result})

@app.route('/plot_graph', methods=['POST'])
def plot_graph():
    function = request.form.get('function')
    try:
        # Convert the function to a callable
        x = sp.symbols('x')
        func = sp.lambdify(x, sp.sympify(function), 'numpy')

        # Generate x and y values
        x_vals = np.linspace(-10, 10, 400)
        y_vals = func(x_vals)

        # Plotting the graph
        plt.figure(figsize=(5, 5))
        plt.plot(x_vals, y_vals)
        plt.title(f"Graph of {function}")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid(True)

        # Save the plot to a PNG image in memory
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)

        # Encode the image as Base64
        img_b64 = base64.b64encode(img.read()).decode('utf-8')
        return jsonify({'img_b64': img_b64})
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/calculate_derivative', methods=['POST'])
def calculate_derivative_route():
    function = request.form.get('function')
    result = calculate_derivative(function)
    return jsonify(result=result)

@app.route('/calculate_integral', methods=['POST'])
def calculate_integral_route():
    function = request.form.get('function')
    indefinite_integral, definite_integral = calculate_integral(function)
    return jsonify(indefinite_integral=indefinite_integral, definite_integral=definite_integral)

@app.route('/calculate_limit', methods=['POST'])
def calculate_limit_route():
    function = request.form.get('function')
    result = calculate_limit(function)
    return jsonify(result=result)

if __name__ == "__main__":
    app.run(debug=True)
    