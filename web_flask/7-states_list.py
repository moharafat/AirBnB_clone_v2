#!/usr/bin/python3
"""
starts a Flask web application
"""
from flask import Flask, render_template
from models.state import State
from models import *
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def statelists():
    """listing states"""
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda x: x.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def teardown(exception):
    """Remove current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
