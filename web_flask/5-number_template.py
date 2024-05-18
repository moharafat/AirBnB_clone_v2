#!/usr/bin/python3
"""
starts a Flask web application
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_HBNB():
    """
    returns Hello HBNB
    """

    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """
    returns HBNB
    """

    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C_DESC(text):
    """
    c +Replace underscores with spaces
    """
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def des(text):
    """
    Displays 'Python' followed by the text
    """
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def html(n):
    """
    display a HTML page
    """
    return n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_page(n):
    """
    Number template
    """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
