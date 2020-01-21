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


@app.route('/c/<text>')
def _text_random(text):
    """prints random text"""
    strict_slashes = False
    if '_' in text:
        text.replace(" ")
    return 'C {}'.format(text)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
