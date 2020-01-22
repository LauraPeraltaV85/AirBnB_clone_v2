#!/usr/bin/python3
""" Flask"""
from flask import Flask, render_template
from models import storage, State
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(self):
    """remove current SQLAlchemy session"""
    storage.close()


@app.route('/states_list')
def states_list():
    """prints states list"""
    strict_slashes = False
    states = storage.all("State")
    stat = dict()
    for key, value in states.items():
        if "State" in key:
            stat[key] = value
    return render_template("7-states_list.html", states=stat)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
