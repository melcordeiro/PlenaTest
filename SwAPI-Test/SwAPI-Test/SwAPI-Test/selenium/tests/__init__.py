from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest, time

import os

class SelinumTest(object):
    driver = None
    base_url = "https://swapi.dev/api/"


class SelinumLoginTest(SelinumTest):
    base_url = SelinumTest.base_url

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        # cls.driver = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def setUp(self):
        super().setUp()
        self.login()
