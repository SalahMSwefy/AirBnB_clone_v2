#!/usr/bin/python3
''' Script that starts a Flask web application '''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Return a string"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return a string when /hbnb is called"""
    return "HBNB"


if __name__ == '__main__':
    app.run(debug=True, port=5000)
