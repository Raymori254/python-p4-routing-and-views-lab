#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
@app.route('/')

def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(f"{parameter}")
    return f"{parameter}"
    
@app.route('/count/<int:parameter>')
def count(parameter):
    count = '\n'.join(str(i) for i in range(parameter)) + '\n'
    return count

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    num1 = float(num1)
    num2 = float(num2)
    
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '%':
            result = num1 % num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
            return f"{result:.1f}"
        else:
            return "<h1>Error: Division by zero</h1>"
    else:
        return "<h1>Error: Invalid operation</h1>"
    
    if isinstance(result, float) and result.is_integer():
            return str(int(result))
    return str(result)