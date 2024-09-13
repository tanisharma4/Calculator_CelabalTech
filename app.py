from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Route to render the calculator.html template
@app.route('/')
def index():
    return render_template('calculator.html')

# Route to handle arithmetic operations
@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Get data from form submission
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operator = request.form['operator']

        # Perform calculation based on operator
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ValueError("Division by zero")
            result = num1 / num2
        else:
            return jsonify({'error': 'Invalid operator'})

        # Return JSON response with result
        return jsonify({'result': result})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
