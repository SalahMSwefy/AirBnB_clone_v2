#!/usr/bin/python3
''' Script that starts a Flask web application '''
from flask import Flask, render_template
from models import storage
from models.state import State
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


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Return a string when /states_list is called"""
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
