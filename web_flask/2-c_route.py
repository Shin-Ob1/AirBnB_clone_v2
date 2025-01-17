#!/usr/bin/python3
"""The application listens on 0.0.0.0, port 5000"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Display 'hello hbnb' """
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def only_hbnb():
    """ Display hbnb """
    return ('HBNB')


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays 'C' and the value of <text>."""
    text = text.replace("_", " ")
    return ('C' + ' ' + text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
