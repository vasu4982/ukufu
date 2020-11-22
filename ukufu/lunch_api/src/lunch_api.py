"""
This file contains all REST APIs and works like a gateway for the application
"""

from flask import Flask
from flask_restplus import fields, marshal
from flask_restplus import Resource, Api
from datetime import date

from .lunch_manager import LunchManager
from .app_logger import get_logger

__author__ = "Narendra Allam"
__copyright__ = "Copyright 2020, Twch Task, ukufu.com"
__credits__ = ["Narendra Allam"]
__license__ = "GPL"
__maintainer__ = "Narendra Allam"
__email__ = "naren@rossum.io"
__status__ = "Development"


app = Flask(__name__)
api = Api(app, version='1.0',
		       title='Lunch Manger API',
               description='All possible recipes for Lunch with available fresh ingredients',)

# logger instance
logger = get_logger("LunchAPI")

# Namespaces
lunch = api.namespace('lunch', description='Public API')

# Lunch Manager
lunch_instance = LunchManager()

# Serializer Model for Testing
TestDateModel = api.model("TestDateModel", {'date': fields.Date(required=False, default=date(2021, 3, 26))})

# Main API
@lunch.route("/")
class LunchMenu(Resource):
	def get(self):
		"""Returns all possible recipes for Lunch Menu"""
		return {"menu": lunch_instance.get_menu()}, 200

@lunch.route("/<string:_date>/")
class LunchMenuForDate(Resource):
	def get(self, _date):
		"""Returns all possible recipes for Lunch Menu for the given date (for Testing)"""
		logger.debug(_date)
		_date = date(*[int(x) for x in _date.split('-')])
		return {"menu": lunch_instance.get_menu(_date)}, 200


@lunch.route("/getupdateddata/")
class LoadData(Resource):
	def get(self):
		"""Retrieves data from data API"""
		return {
			"status": lunch_instance.get_updated_data()
		}, 200


# Business Case 1: Maximizing number of recipes with non overlapping ingredients
@lunch.route("/optimal/")
class OptimalLunchMenu(Resource):
	def get(self):
		"""
		Returns recipes (Optimal case: Uses exact cover, max cover approach)
		"""
		return {
			"status": "TO BE DONE"
		}


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)

