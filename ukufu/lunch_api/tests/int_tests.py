"""This file contains Integration Tests for Few REST APIs"""

import urllib3
import json
from unittest import TestCase, main
from Src.app_logger import get_logger

__author__ = "Narendra Allam"
__copyright__ = "Copyright 2020, Tech Task, ukufu.com"
__credits__ = ["Narendra Allam"]
__license__ = "GPL"
__maintainer__ = "Narendra Allam"
__email__ = "naren@rossum.io"
__status__ = "Development"


# logger instance
logger = get_logger("IntTests")

class TestLunchAPI(TestCase):
    def setUp(self):
        """
        Dumping data from JSON to in-memory data structures
        Getting test data ready
        """
        try:
            self.http = urllib3.PoolManager()
            url = 'http://127.0.0.1:5000/data/load/'
            resp = self.http.request('GET', url)
            data = json.loads(resp.data.decode('utf-8'))

        except Exception as ex:
            logger.error(ex)
        else:
            logger.info(data)

    def tearDown(self):
        del self.http

    def test_get_menu_api(self):
        # Testing get_menu_api
        try:
            url = 'http://127.0.0.1:8000/lunch/'
            resp = self.http.request('GET', url)
            data = json.loads(resp.data.decode('utf-8'))
            logger.debug(data)
            self.assertTrue(data == {'menu': ['Ham and Cheese Toastie', 'Salad', 'Hotdog']})

        except Exception as ex:
            logger.error(ex)
        else:
            logger.info(data)

        # Adding New Recipe to Data
        try:
            new_recipe = {
                "name": "Toastie",
                "ingredients": [
                    "Ham",
                    "Butter",
                    "Bread"
                ]
            }

            payload = new_recipe
            url = 'http://127.0.0.1:5000/recipe_crud/createupdate/'
            encoded_data = json.dumps(payload)
            resp = self.http.request('POST', url, body=encoded_data, headers={'Content-Type': 'application/json'})
            data = json.loads(resp.data)
            logger.debug(data)
            self.assertTrue(data['status'] == 'Recipe Added Successfully!')

        except Exception as ex:
            logger.error(ex)
        else:
            logger.info(data)

        # Retrieving updated data from Data API
        try:
            url = 'http://127.0.0.1:8000/lunch/getupdateddata/'

            resp = self.http.request('GET', url)
            data = json.loads(resp.data)

        except Exception as ex:
            logger.error(ex)
        else:
            logger.info(data)

        # Testing for a specific date 
        try:
            url = 'http://127.0.0.1:8000/lunch/2021-3-26/'

            resp = self.http.request('GET', url)
            data = json.loads(resp.data)
            logger.debug(data)
            self.assertTrue(data == {'menu': ['Toastie', 'Hotdog']})
        except Exception as ex:
            logger.error(ex)
        else:
            logger.info(data)

if __name__ == "__main__":
    main()