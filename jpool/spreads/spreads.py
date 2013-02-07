__author__ = 'Andrew Hawker <andrew.r.hawker@gmail.com'

from flask import Blueprint, jsonify
from jpool.spreads.constants import MOCK_SPREADS

spreads = Blueprint('spreads', __name__, url_prefix='/api/spreads')

@spreads.route('/')
def get_spreads():
	return jsonify(spreads=MOCK_SPREADS)

@spreads.route('/<int:year>')
def get_spreads_by_year(year):
	return jsonify(spreads=MOCK_SPREADS[2012-year])

@spreads.route('/<int:year>/<int:week>')
def get_spreads_by_week(year, week):
	return jsonify(spreads=MOCK_SPREADS[2012-year][week-1])