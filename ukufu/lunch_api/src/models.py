"""
This file contains definitions for core entities Recipes and Ingredients
"""

from datetime import date

__author__ = "Narendra Allam"
__copyright__ = "Copyright 2020, Tech Task, ukufu.com"
__credits__ = ["Narendra Allam"]
__license__ = "GPL"
__maintainer__ = "Narendra Allam"
__email__ = "naren@rossum.io"
__status__ = "Development"

class Ingredient(object):
    """ Ingredient expiry details
        Attributes:
            name: string
            best_before: datetime.date
            use_by: datetime.date
    """
    def __init__(self, _name=None, _best_before=None, _use_by=None):
        self.name = _name
        year, month, day =[int(x) for x in _best_before.split('-')]
        self.best_before = date(year, month, day)
        year, month, day =[int(x) for x in _use_by.split('-')]
        self.use_by = date(year, month, day)

    def __hash__(self):
        return hash(self.name)
    
    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return f"name: {self.name}, best_before: {self.best_before}, use_by: {self.use_by}"

    def __repr__(self):
        return f"Ingredient('{self.name}', '{self.best_before}', '{self.use_by}')"

class Recipe(object):
    """ Recipe's ingredient details
        Attributes: 
            name: string
            ingredients: list of all ingredients
    """
    def __init__(self, title=None, ingredients=[]):
        self.name = title
        self.ingredients = set(ingredients)


    def __str__(self):
        return f"name: {self.name}, ingredients: {self.ingredients}"

    def __repr__(self):
        return f"Recipe('{self.name}', {self.ingredients})"

        self.recipes = {"Salad": Recipe(name="Salad", ingredients=['ham', 'lettuce']), }