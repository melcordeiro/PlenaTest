from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest, time

import os

class SeliniumTest(object):
    driver = None
    url = 'www.globo.com'
    busca = 'Corona Virus'
    data_selecao = "Período personalizado"
    data = '01/08/2020'

    #path_download="/home/mhvithoft/Downloads/"
    #folder_images = "~/Pictures/"
    #path_download = os.path.expanduser("~") + "/Downloads/"


    # pegando o path atual da execução dos testes
    current_path = os.getcwd()
    pos = current_path.find("selenium")
    if pos > 0:
    #    print("path = " + current_path[0:pos])
        folder_images = current_path[0:pos] + "selenium/tests/captura/"

class SelinumAccessTest(SeliniumTest):
    url = SeliniumTest.url
   # folder_images = SeliniumTest.folder_images


    def access(self):
        self.driver.get(self.url)
        time.sleep(2)

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
