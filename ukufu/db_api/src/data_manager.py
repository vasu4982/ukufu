"""
This file containins all data related functionalities.
DataManager class works like a DB and can also be used
to provide test data for testting
"""

import json
from json import JSONDecodeError
import pickle
from pickle import PicklingError, UnpicklingError
from datetime import date

from .app_logger import get_logger
from .config import INGREDIENTS_DATA_FILE, RECIPES_DATA_FILE
from .config import INGREDIENTS_PICKLE_FILE, RECIPES_PICKLE_FILE
from .models import Recipe, Ingredient

__author__ = "Narendra Allam"
__copyright__ = "Copyright 2020, Tech Task, ukufu.com"
__credits__ = ["Narendra Allam"]
__license__ = "GPL"
__maintainer__ = "Narendra Allam"
__email__ = "naren@rossum.io"
__status__ = "Development"

# logger instance
logger = get_logger("DataManagerAPI")


class DataManager(object):
    """ Manages all data requirements.

    Managing data at various phases of the application, 
    includes migration, backup and recovery.

    Attributes:
        ingredients: dict type, Key: Ingredient, Value: Ingredient Object
        recipes: dict type, Key: Recipe, Value: set() of Ingredient Objects
    """
    def __init__(self):
        self.ingredients = {}
        self.recipes = {}
        self.parse_data()

    # Recipe CRUD Operations
    def add_update_recipe(self, recipe):
        """ add/update recipe"""
        status = "Recipe Added Successfully!"

        if recipe['name'] in self.recipes:
            status = "Recipe Updated Successfully!"

        self.recipes[recipe['name']] = Recipe(recipe['name'], recipe['ingredients'])
        logger.info(status)
        return status
    
    def get_all_recipes(self):
        """ Returns all recipes"""
        logger.info(self.recipes)
        return self.recipes

    def read_recipe(self, name):
        """ Returns recipes details """
        logger.info(self.recipes.get(name))
        return self.recipes.get(name)

    def del_recipe(self, name):
        """ Deletes recipe if exists"""
        status = ""
        if name in self.recipes:
            self.recipes.pop(name)
            status = "Successfully deleted!"
        else:
            status = "Key not found!"

        logger.info(status)
        return status

    # Ingredient CRUD Operations
    def add_update_ingredient(self, ingredient):
        """ add/update ingredient"""
        status = "Ingredient Added Successfully!"

        if ingredient['name'] in self.ingredients:
            status = "Ingredient Updated Successfully!"

        self.ingredients[ingredient['name']] =  Ingredient(ingredient['name'], 
                                                           ingredient['best_before'],
                                                           ingredient['use_by'])
        logger.info(status)
        return status

    def get_all_ingredients(self):
        """ Returns all Ingredients available """
        logger.info(self.ingredients)
        return self.ingredients

    def read_ingredient(self, name):
        """ Returns ingredient details"""
        logger.info(self.ingredients.get(name))
        return self.ingredients.get(name)

    def del_ingredient(self, name):
        """ Deletes recipe if exists"""
        status = ""
        if name in self.ingredients:
            self.ingredients.pop(name)
            status = "Success fully deleted!"
        else:
            status = "Key not found!"

        logger.info(status)
        return status

    def parse_data(self):
        """
        Loads data from json files to data structures. 
        Generally used when server is reset.

        Returns:
            error_msg: error or success message
        """
        status_msg = ""
        # Parsing ingredients.json
        try:
            
            with open(INGREDIENTS_DATA_FILE) as f:
                _ingredients = json.load(f)["ingredients"]
                for ingredient in _ingredients:
                    self.ingredients[ingredient['title']] = Ingredient(ingredient['title'], 
                                                                       ingredient['best-before'],
                                                                       ingredient['use-by'])
            logger.info(f"{INGREDIENTS_DATA_FILE} Successfully parsed;")
        except (JSONDecodeError, KeyError) as ex:
            status_msg += f"While parsing json file: {INGREDIENTS_DATA_FILE} encountered error: {ex};"
            logger.error(status_msg)
        else:
            status_msg += f"File:'{INGREDIENTS_DATA_FILE}' parsed successfully!;"

        # Parsing recipes.json
        try:
            with open(RECIPES_DATA_FILE) as f:
                _recipes = json.load(f)["recipes"]
                for recipe in _recipes:
                    self.recipes[recipe['title']] = Recipe(recipe['title'], recipe['ingredients'])
            logger.info(f"{RECIPES_DATA_FILE} Successfully parsed;")
        except (JSONDecodeError, KeyError) as ex:
            status_msg += f"While parsing json file: {RECIPES_DATA_FILE} encountered error: {ex};"
            logger.error(status_msg)
        else:
            status_msg += f"File:'{RECIPES_DATA_FILE}' parsed successfully!;"

        return status_msg

    def save_data(self):
        """
        Saves data to disk(pickle files) from data structures. 
        Generally used before server restarted for maintainance.

        Returns:
            error_msg: error or success message
        """
        status_msg = ""

        try:
            with open(INGREDIENTS_PICKLE_FILE, "wb") as f:
                pickle.dump(self.ingredients, f, pickle.HIGHEST_PROTOCOL)
        except PicklingError as ex:
            status_msg += f"While pickling 'Ingredients' encountered error: {ex};"
            logger.error(status_msg)           
        else:
            status_msg += f"Data backup to: '{INGREDIENTS_PICKLE_FILE}'has been successfull!"
            logger.info(status_msg)

        try:
            with open(RECIPES_PICKLE_FILE, "wb") as f:
                pickle.dump(self.recipes, f, pickle.HIGHEST_PROTOCOL)
        except PicklingError as ex:
            status_msg += f"While pickling 'Recipes' encountered error: {ex};"
        else:
            status_msg += f"Data backup to: '{RECIPES_PICKLE_FILE}'has been successfull!"
            logger.error(status_msg)

        return status_msg

    def load_data(self):
        """
        Loads data from pickle files to data structures. 
        Generally used when server restarted for maintainance.

        Returns:
            error_msg: error or success message
        """
        status_msg = ""
        try:
            with open(INGREDIENTS_PICKLE_FILE, "rb") as f:
                self.ingredients = pickle.load(f)
        except UnpicklingError as ex:
            status_msg += f"While un pickling '{INGREDIENTS_PICKLE_FILE}' encountered error: {ex};"
            logger.error(status_msg) 
        else:
            status_msg += f"Data reloaded from: '{INGREDIENTS_PICKLE_FILE} successfully!;"
            logger.error(status_msg)    
        
        try:
            with open(RECIPES_PICKLE_FILE, "rb") as f:
                self.recipes = pickle.load(f)
        except UnpicklingError as ex:
            status_msg += f"While Unpickling '{RECIPES_PICKLE_FILE}' encountered error: {ex};"
        else:
            status_msg += f"Data reloaded from: '{RECIPES_PICKLE_FILE} successfully!;"
            logger.error(status_msg)    
             
        logger.debug(self.recipes)
        return status_msg


# Data Instance, works as a DB
data_instance = DataManager()
