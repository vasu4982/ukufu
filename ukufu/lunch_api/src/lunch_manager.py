"""
This file contains core logic of the application, which is to provide CRUD operations
to Ingredients and Recipes and preparing menu with possible recipes from available 
Ingredients.
"""

from datetime import date
import urllib3
import json

from .models import Recipe, Ingredient
from .app_logger import get_logger

__author__ = "Narendra Allam"
__copyright__ = "Copyright 2020, Tech Task, ukufu.com"
__credits__ = ["Narendra Allam"]
__license__ = "GPL"
__maintainer__ = "Narendra Allam"
__email__ = "naren@rossum.io"
__status__ = "Development"

# logger instance
logger = get_logger("LunchAPI")

class LunchManager(object):
    """ Lunch Menu
        Core component of application. Providing menu with all available recipes.
    """

    def __init__(self):
        self.recipes = {}
        self.ingredients = {}
        self.http = urllib3.PoolManager()
        self.get_updated_data()
        
    def get_updated_data(self):
        """
        Loads data from data API
        """
        status = ""
        try:
            url = 'http://db_api:5000/recipe_crud/allrecipes/'
            resp = self.http.request('GET', url)
            data = json.loads(resp.data.decode('utf-8'))
            self.recipes = {}
            for recipe in data:
                self.recipes[recipe['name']] = Recipe(recipe['name'], recipe['ingredients'])

        except Exception as ex:
            logger.error(ex)
            status += str(ex)
        else:
            logger.debug(self.recipes)
            status += "All Recipes retrieved from data API;"

        try:
            url = 'http://db_api:5000/ingredient_crud/allingredients/'
            resp = self.http.request('GET', url)
            data = json.loads(resp.data.decode('utf-8'))
            self.ingredients = {}
            for ingred in data:
                self.ingredients[ingred['name']] = Ingredient(ingred['name'], 
                                                              ingred['best_before'],
                                                              ingred['use_by'])
        except Exception as ex:
            logger.error(ex)
            status += str(ex)
        else:
            logger.debug(self.ingredients)
            status += "All Ingredients retrieved from data API;"

        return status

    # very important ***
    def get_menu(self, cur_date=date.today()):
        """ Params:
                cur_date: datetime.date (Optional)
            Returns: 
                Lunch Menu with all recipes
        """

        # Get all available ingredients
        usable_ingredients = set()
        not_fresh_ingredients = set()

        for _, obj in self.ingredients.items():
            # by Use-by date
            if obj.use_by >= cur_date:
                usable_ingredients.add(obj.name)
                # by best-before
                if obj.best_before < cur_date:
                    not_fresh_ingredients.add(obj.name)

        logger.debug("-"*20)
        logger.debug(f"usable ingredients:{usable_ingredients}")
        logger.debug(f"not fresh ingredients: {not_fresh_ingredients}")
        logger.debug("-"*20)

        # All possible recipes with available_ingredients
        serviceable_recipes = []
        fresh_recipes = []
        for _, obj in self.recipes.items():
            # by available ingredients
            if obj.ingredients.issubset(usable_ingredients):
                # by best-before
                stale_count = len(obj.ingredients & not_fresh_ingredients)
                if stale_count:
                    serviceable_recipes.append((obj.name, stale_count))
                else:
                    fresh_recipes.append(obj.name) 
        logger.debug("-"*20)            
        logger.debug(f"fresh recieps: {fresh_recipes}")
        logger.debug(f"serviceable recipes: {serviceable_recipes}")
        logger.debug("-"*20)
        # Sorting menu based on freshness
        serviceable_recipes.sort(key=lambda x:x[1])
        # Fresh recipes first
        fresh_recipes.extend([item for item, count in serviceable_recipes])

        logger.info(fresh_recipes)
        return fresh_recipes

