__author__ = 'Andrew Hawker <andrew.r.hawker@gmail.com>'

from flask import Blueprint

scores = Blueprint('scores', __name__, url_prefix='/api/scores')

@scores.route('/')
def f():
	return 'hello world'