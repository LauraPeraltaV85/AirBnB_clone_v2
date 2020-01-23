#!/usr/bin/python3
""" Flask"""
from flask import Flask, render_template
from models import storage, State, City, Amenity
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(self):
    """remove current SQLAlchemy session"""
    storage.close()


@app.route('/hbnb_filters')
def states_filter(idn=None):
    """print filtered states"""
    strict_slashes = False
    states = storage.all("State")
    cities = storage.all("City")
    amenities = storage.all("Amenity")
    cit = dict()
    stat = dict()
    am = dict()
    for key, value in states.items():
        if "City" in key:
            cit[key] = value
        if "State" in key:
            stat[key] = value
        if "Amenity" in key:
            am[key] = value
    return render_template("10-hbnb_filters.html", cities=cit, states=stat, amenities=am)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
