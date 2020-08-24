# -*- encoding: utf-8 -*-
import time
import unittest
import uuid
import json
from builtins import Exception

import requests

class AccessSwAPI(unittest.TestCase):

    endpoint="https://swapi.dev/api/"
    headers = {'Content-Type': 'application/json'}
    timeout_post = 45

    # método público - não requer autenticação
    def test_Access_successfully(self):
        print('test_Access_successfully')
        print(self.endpoint)

        try:
            feedback = requests.get(self.endpoint,  timeout=self.timeout_post)

            if 200 == feedback.status_code:
                print("\t[test_Access_successfully] SUCESSO\n")
            else:
                raise Exception
        except Exception as exception:
            raise exception


    def test_get_lista_planeta_nome(self):
        print('test_get_lista_planeta_nome')

        try:
            nome = 'alderaan'

            feedback = requests.get(self.endpoint + "planets/?search=%s" %nome, timeout=self.timeout_post)

            if 200 == feedback.status_code:
                print ("Planeta %s = " %nome + str(feedback.json()))
                print("\t[test_get_lista_planeta_nome] SUCESSO\n")
            else:
                raise Exception
        except Exception as exception:
            raise exception

    def test_get_lista_planetas(self):
        print('test_get_lista_planetas')

        try:
            feedback = requests.get(self.endpoint + "planets/", timeout=self.timeout_post)

            if 200 == feedback.status_code:
                print ("Lista Planetas = " + str(feedback.json()))
                print("\t[test_get_lista_planeta] SUCESSO\n")
            else:
                raise Exception
        except Exception as exception:
            raise exception

    def test_get_lista_filmes(self):
        print('test_get_lista_filmes')

        try:
            feedback = requests.get(self.endpoint + "films/", timeout=self.timeout_post)

            if 200 == feedback.status_code:
                print("Lista Filmes = " + str(feedback.json()))
                print("\t[test_get_lista_filmes] SUCESSO\n")
            else:
                raise Exception
        except Exception as exception:
            raise exception

    #Traz a url e os nomes dos filmes que o planeta Alderaan aparece
    def test_get_count_planeta_alderaan_filmes(self):
        print('test_get_count_planeta_alderaan_filmes')
        try:
            feedback = requests.get(self.endpoint + "planets/", timeout=self.timeout_post, headers=self.headers)
            feedback2 = requests.get(self.endpoint + "films/", timeout=self.timeout_post, headers=self.headers)

            if 200 == feedback.status_code and 200 == feedback2.status_code:
                #print("Lista Filmes = " + str(feedback.json()))
                data = json.loads(feedback.text)
                data2 = json.loads(feedback2.text)

                output_film = []
                output_filmname = []

                # Preenche a lista com as URLs dos filmes que Alderaan aparece
                for filmes in data['results']:
                    if len(filmes['films']) > 0 and filmes['name'] == "Alderaan":
                        for f in filmes['films']:
                            output_film.append(f)

                # Preenche a lista com os nomes dos filmes que Alderaan aparece
                for nomes in data2['results']:
                    for k in output_film:
                        if nomes['url'] == k:
                            output_filmname.append(nomes['title'])


                print("URL Filmes: %s" % (output_film))
                print("Nome Filmes: %s" % (output_filmname))

                print("\t[test_get_count_planeta_alderaan_filmes] SUCESSO\n")
            else:
                raise Exception
        except Exception as exception:
            raise exception