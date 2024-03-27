#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:string>')
def print_string(string):
    print(string)
    return f'{string}'

@app.route('/count/<int:parameter>')
def count(parameter):
    answer = ''
    for num in range(parameter):
        answer += f'{str(num)}\n'
    return answer
# - A `math()` view should take three parameters: `num1`, `operation`, and `num2`.
#   It must perform the appropriate operation on the two numbers in the order that
#   they are presented. The included operations should be: `+`, `-`, `*`, `div`
#   (`/` would change the URL path), and `%`. Its URL should be of the format
#   `/math/<num1>/<operation>/<num2>`.
@app.route('/math/<int:num1>/<string:operator>/<int:num2>')
def math(num1, operator, num2):
    if operator == "+":
        return str(num1 + num2)
    elif operator == "-":
        return str(num1 - num2)
    elif operator == "*":
        return str(num1 * num2)
    elif operator == "div":
        return str(num1 / num2)
    elif operator == "%":
        return str(num1 % num2)

if __name__ == '__main__':
    app.run(port=5555, debug=True)