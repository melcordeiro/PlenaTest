# -*- encoding: utf-8 -*-
import os
import time
import unittest

from selenium import webdriver

class BuscaTest(unittest.TestCase):
    driver = None

    url = "https://www.globo.com/"
    busca = 'Corona Virus'
    data_selecao = "Período personalizado"

    # pegando o path atual da execução dos testes
    current_path = os.getcwd()
    pos = current_path.find("selenium")
    if pos > 0:
        folder_images = current_path[0:pos] + "selenium/tests/captura/"

    @classmethod
    def setUpClass(cls):
        super(BuscaTest, cls).setUpClass()
        if cls.driver is None:
            cls.driver = webdriver.Chrome('C:\\chromedriver.exe') #inserir o caminho onde o chromedriver.exe está alocado

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super(BuscaTest, cls).tearDownClass()

    def setUp(self):
        self.driver.delete_all_cookies()

    def tearDown(self):
        self.driver.execute_script("window.sessionStorage.clear();")
        self.driver.execute_script("window.localStorage.clear();")
        #print ("tearDown()")

        pass

    def test_access_busca(self):
            try:
                self.driver.maximize_window()
                self.driver.get(self.url)
                time.sleep(2)
    
                self.assertEqual(self.url, self.driver.current_url)
                print("Site Equivalente - SUCESSO")
    
                #Realiza primeira busca por Corona Virus
                self.driver.find_element_by_class_name('home-header__search').click()
                time.sleep(2)
                self.driver.find_element_by_name('q').send_keys(self.busca)
                self.driver.find_element_by_class_name('home-header__search-button').click()
                time.sleep(2)
                print("Busca por título realizada - SUCESSO")
    
                #Seleciona dia 01/08/2020 por filtragem de data por período específico
                self.driver.find_element_by_xpath("//*[@id='search-filter-component']/div/div[1]/div/div/div[2]/div/a/span[1]").click()
                self.driver.implicitly_wait(10)
                self.driver.find_element_by_xpath("//*[@id='search-filter-component']/div/div[1]/div/div/div[2]/div/ul/li[8]/span").click()
                self.driver.find_element_by_xpath("//*[@id='search-filter-component']/div/div[1]/div/div/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[7]").click()
                self.driver.implicitly_wait(10)
                self.driver.find_element_by_xpath("//*[@id='search-filter-component']/div/div[1]/div/div/div[2]/div[1]/div/div[3]/button").click()
                time.sleep(2)
                #time.sleep(2)
                print("Busca por Período Personalizado - SUCESSO")
    
                # Captura da tela de busca com filtros por pesquisa e data
                self.driver.save_screenshot(self.folder_images+'busca.png')
                print("Captura de Busca salva em pasta específica criada no projeto - SUCESSO")
    
                ##content > div > div > ul > li:nth-child(21) > div.widget--info__text-container > a
                #fazer while para rodar paginação enquanto não achar
                #scroll
                last_height =self.driver.execute_script("return document.body.scrollHeight")
                while True:
                    self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                    time.sleep(2)
                    new_hight = self.driver.execute_script("return document.body.scrollHeight")
                    if new_hight == last_height:
                         break
                    last_height = new_hight

                self.driver.implicitly_wait(10)
                self.driver.find_element_by_partial_link_text('Rússia anuncia vacinação em massa contra o coronavírus para outubro').click()
                time.sleep(2)

                # Gerar arquivo texto
                conteudo = self.driver.find_elements_by_class_name("mc-article-body")
                for c in conteudo:
                    #print(c.text)
                    arquivo = open(self.folder_images+'conteudo_noticia.txt', 'w')
                    arquivo.writelines(c.text)
                    arquivo.close()

                print("Criação de txt com conteúdo de notícia salva em pasta específica criada no projeto - SUCESSO")

                # Captura notícia
                self.driver.save_screenshot(self.folder_images + 'noticia.png')
                print("Captura de notícia salva em pasta específica criada no projeto - SUCESSO")


                print("[test_access_busca] SUCESSO")
            except Exception as exception:
                print("[test_access_busca] FALHA")
                raise exception

