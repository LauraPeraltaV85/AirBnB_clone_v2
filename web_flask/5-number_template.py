#!/usr/bin/python3
"""Hello Flask"""
from flask import Flask, render_template
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
        text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/<text>')
@app.route('/python')
@app.route('/python/')
def _text_random_python(text='is cool'):
    """prints random text python"""
    strict_slashes = False
    if '_' in text:
        text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>')
def _number(n):
    """prints random number"""
    strict_slashes = False
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def _number_template(n):
    """prints random number template"""
    strict_slashes = False
    return render_template('5-number.html', num=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
