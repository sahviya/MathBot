function solveBasic() {
    var expression = document.getElementById('basic_expression').value;
    fetch('/basic_operations', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: 'expression=' + encodeURIComponent(expression)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('basic_result').innerText = "Result: " + data.result;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function solveEquation() {
    var equation = document.getElementById('equation_input').value;
    fetch('/solve_equations', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: 'equation=' + encodeURIComponent(equation)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('equation_result').innerText = "Solutions: " + data.result;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function calculateTrigonometricDerivative() {
    var functionInput = document.getElementById('trig_function').value;

    // Ensure the input is not empty
    if (!functionInput.trim()) {
        document.getElementById('trig_result').innerText = "Error: Please enter a valid trigonometric function.";
        return;
    }

    fetch('/trigonometric', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ function: functionInput })  // Match the backend key name
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);  // Log the response to see what Flask returns
        if (data.error) {
            document.getElementById('trig_result').innerText = "Error: " + data.error;
        } else if (data.result) {
            document.getElementById('trig_result').innerText = "Result: " + data.result;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('trig_result').innerText = "Error: Unable to process the request.";
    });
}

function plotGraph() {
    var functionInput = document.getElementById('graph_function').value; // Get the input from the text box
    fetch('/plot_graph', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: 'function=' + encodeURIComponent(functionInput)
    })
    .then(response => response.json()) // Parse JSON response
    .then(data => {
        if (data.img_b64) {
            // Set the graph image's source to the Base64 image
            document.getElementById('graph_img').src = 'data:image/png;base64,' + data.img_b64;
        } else {
            alert('Error: ' + (data.error || 'Unable to plot graph.'));
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while trying to plot the graph.');
    });
}


function calculateDerivative() {
    var functionInput = document.getElementById('derivative_function').value;
    fetch('/calculate_derivative', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: 'function=' + encodeURIComponent(functionInput)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('derivative_result').innerText = "Derivative: " + data.result;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function calculateIntegral() {
    var functionInput = document.getElementById('integral_function').value;
    fetch('/calculate_integral', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: 'function=' + encodeURIComponent(functionInput)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('integral_result').innerText = "Indefinite Integral: " + data.indefinite_integral;
        document.getElementById('definite_integral_result').innerText = "Definite Integral (from 0 to 1): " + data.definite_integral;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function calculateLimit() {
    var functionInput = document.getElementById('limit_function').value;
    fetch('/calculate_limit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: 'function=' + encodeURIComponent(functionInput)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('limit_result').innerText = "Limit as x approaches 1: " + data.result;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
