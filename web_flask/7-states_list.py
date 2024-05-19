#!/usr/bin/python3
"""
starts a Flask web application
"""
from flask import Flask, render_template
app = Flask(__name__)


storage.close()

@app.route('/states_list', strict_slashes=False)
def HBNB():
    """
    returns HBNB
    """

    return 'HBNB'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
