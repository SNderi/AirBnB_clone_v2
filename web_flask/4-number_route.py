#!/usr/bin/python3
""" Script that starts a Flask web application. """

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Returns Hello hbnb. """
    return 'Hello, HBNB!'


@app.route('/hbnb', strict_slashes=False)
def shout_hbnb():
    """ Returns hbnb. """
    return 'HBNB!'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ Returns C followed by a text with _ replaced by spaces. """
    text = text.replace("_", " ")
    return 'C {}'.format(text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_text(text="is cool"):
    """ Returns Python followed by a text with _ replaced by spaces. """
    text = text.replace("_", " ")
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def check_int(n):
    """ Returns “n is a number” only if n is an integer. """
    return '{} is a number'.format(n)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
