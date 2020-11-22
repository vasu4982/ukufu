"""This file contains Unit Tests for Core Lunch Manager API"""

from unittest import TestCase, main
from datetime import date
import mock

from Src.lunch_manager import LunchManager
from Src.data_manager import DataManager
from Src.app_logger import get_logger

__author__ = "Narendra Allam"
__copyright__ = "Copyright 2020, Tech Task, ukufu.com"
__credits__ = ["Narendra Allam"]
__license__ = "GPL"
__maintainer__ = "Narendra Allam"
__email__ = "naren@rossum.io"
__status__ = "Development"


# logger instance
logger = get_logger("UnitTests")

class TestLunchManger(TestCase):
    """
    Test Class for Lunch Manager
    """
    def setUp(self) -> None:
        self.lunch_instance = LunchManager()

    def tearDown(self) -> None:
        del self.lunch_instance

    def test_get_menu(self):

        expected_output1 = ["Hotdog"]
        output = self.lunch_instance.get_menu(date(2021, 3, 26))
        logger.info(output)
        self.assertTrue(output == expected_output1)

        expected_output2 = ["Toastie", "Hotdog"]
        self.data_instance.add_update_recipe({
            "name": "Toastie",
            "ingredients": [
                "Butter",
                "Ham",
                "Bread"
            ]
        })
        output = self.lunch_instance.get_menu(date(2021, 3, 26))
        logger.info(output)
        self.assertTrue(output == expected_output2)

    def test_get_optimal_menu(self):
        # To be done
        pass


if __name__ == "__main__":
    main()
