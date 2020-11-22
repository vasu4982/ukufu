
"""
This file contains data specific REST APIs and works like a DB service.
This service can be replaced later with any production Data base.
"""

from flask import Flask
from flask_restplus import fields, marshal
from flask_restplus import Resource, Api
from datetime import date

from .data_manager import data_instance
from .app_logger import get_logger

__author__ = "Narendra Allam"
__copyright__ = "Copyright 2020, Tech Task, ukufu.com"
__credits__ = ["Narendra Allam"]
__license__ = "GPL"
__maintainer__ = "Narendra Allam"
__email__ = "naren@rossum.io"
__status__ = "Development"

app = Flask(__name__)
api = Api(app, version='1.0',
		       title='Data Manager API',
               description='Data Management Service',)
# logger instance
logger = get_logger("DataManagerAPI")

# Namespaces
recipe_crud = api.namespace('recipe_crud', description='Recipe CRUD Ops API')
ingredient_crud = api.namespace('ingredient_crud', description='Ingredient CRUD Ops API')
data = api.namespace('data', description='Internal API')


# Required Serializer models
RecipeModel = api.model("RecipeModel", {
  'name': fields.String,
  'ingredients': fields.List(fields.String)})


IngredientModel = api.model("IngredientModel", {
  'name': fields.String,
  'best_before': fields.Date(default=date.today()),
  'use_by': fields.Date(default=date.today())})

# Recipe CRUD Operations
@recipe_crud.route("/createupdate/")
class CreateUpdateRecipe(Resource):
	@api.expect(RecipeModel)
	def post(self):
		"""Create or Update a Recipe"""
		logger.info(api.payload)
		return {
			"status": data_instance.add_update_recipe(api.payload)
		}


@recipe_crud.route("/allrecipes/")
class GetAllRecipes(Resource):
	@api.marshal_with(RecipeModel)
	def get(self):
		"""Returns all recipes"""
		logger.info(data_instance.get_all_recipes())
		return [v for v in data_instance.get_all_recipes().values()]


@recipe_crud.route("/read/<string:recipe>/")
class ReadRecipe(Resource):
	@api.marshal_with(RecipeModel)
	def get(self, recipe):
		"""Returns details of a single recipe"""
		return data_instance.read_recipe(recipe), 200


@recipe_crud.route("/delete/<string:recipe>/")
class DeleteRecipe(Resource):
	def get(self, recipe):
		"""Deletes a recipes, if exists"""
		return {
			"status": data_instance.del_recipe(recipe)
		}


# Ingredient CRUD Operations
@ingredient_crud.route("/createupdate/")
class CreateUpdateIngredient(Resource):
	@api.expect(IngredientModel)
	def post(self):
		"""Create or update an Ingredient"""
		return {
			"status": data_instance.add_update_ingredient(api.payload)
		}


@ingredient_crud.route("/allingredients/")
class GetAllIngredients(Resource):
	@api.marshal_with(IngredientModel)
	def get(self):
		"""Returns all in available ingredients"""
		logger.info(data_instance.get_all_ingredients())
		return [v for v in data_instance.get_all_ingredients().values()]


@ingredient_crud.route("/read/<string:ingred>/")
class ReadRIngredient(Resource):
	@api.marshal_with(IngredientModel)
	def get(self, ingred):
		""""Returns Ingredient details"""
		return data_instance.read_ingredient(ingred), 200


@ingredient_crud.route("/delete/<string:ingred>/")
class DeleteIngredient(Resource):
	def get(self, ingred):
		"""Deletes an ingredient"""
		return {
			"status": data_instance.del_ingredient(ingred)
		}


@data.route("/load/")
class DataLoader(Resource):
	def get(self):
		"""Loads data from json files to data PAI internal data structures"""
		return {
			"status": data_instance.parse_data()
		}


@data.route("/save/")
class DataSaver(Resource):
	def get(self):
		"""Saves data to respective pickle files from data structures"""
		return {
			"status":data_instance.save_data()
		}

@data.route("/reload/")
class DataReloader(Resource):
	def get(self):
		"""Reloads data from pickle files to data PAI internal data structures"""
		return {
			"status": data_instance.load_data()
		}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)