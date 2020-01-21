#!/usr/bin/python3
"""Hello Flask"""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    """prints hello"""
    strict_slashes = False
    return 'Hello HBNB!'


@app.route('/hbnb')
def _hbnb():
    """prints hbnb"""
    strict_slashes = False
    return 'HBNB'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
