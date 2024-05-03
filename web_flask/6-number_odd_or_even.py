#!/usr/bin/python3
''' Script that starts a Flask web application '''
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Return a string"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return a string when /hbnb is called"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Return a string when /c/<text> is called"""
    message = text.replace("_", " ")
    return "C {}".format(message)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """Return a string when /python/<text> is called"""
    message = text.replace("_", " ")
    return "Python {}".format(message)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Return a string when /number/<n> is called"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Return a string when /number_template/<n> is called"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Return a string when /number_odd_or_even/<n> is called"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
