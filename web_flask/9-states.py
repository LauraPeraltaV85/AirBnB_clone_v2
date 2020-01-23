#!/usr/bin/python3
""" Flask"""
from flask import Flask, render_template
from models import storage, State, City
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(self):
    """remove current SQLAlchemy session"""
    storage.close()


@app.route('/states')
@app.route('/states/<string:idn>')
def states_filter(idn=None):
    """print filtered states"""
    strict_slashes = False
    states = storage.all("State")
    cit = dict()
    stat = dict()
    if idn is None:
        for key, value in states.items():
            if "State" in key:
                stat[key] = value
        return render_template("9-states.html", states=stat, idn=idn)
    else:
        for key, value in states.items():
                if "City" in key:
                    if value.state_id == idn:
                        cit[key] = value
                if "State" in key:
                    if value.id == idn:
                        stat[key] = value
        return render_template("9-states.html", cities=cit, states=stat)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
