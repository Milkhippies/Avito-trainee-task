import utils.fileUtils as fileUtils
from unittest import TestCase
import pytest
import json
import os

class TestCreateErrorJSON(TestCase):

    def test_createErrorJSON_make_exit(self): # делает ли функция прерывание выполнения программы в случае некоректного json
        with self.assertRaises(SystemExit) as cm:
            fileUtils.createErrorJSON("../Result_JSON/error.json","w")
        self.assertEqual(cm.exception.code, 0)

    def test_createErrorJSON_is_correct(self): #правильный ли файл создается при выполненнии функции, сравниваем с эталоном
        with open("../Result_JSON/error.json", "r") as file:
            tested = json.load(file)
        with open("../Reference_JSONs/error.json", "r") as file:
            reference = json.load(file)
        self.assertDictEqual(tested , reference)

    #def test_createErrorJSON_is_dict(self): # является ли получишвийся файл ошибки словарем
    #    with open("../Result_JSON/error.json", "r") as file:
    #        opened = json.load(file)
    #    self.assertIsInstance(opened , dict)


class TestOpenJSON(TestCase):

    def test_openJSON_opened_correct(self): # откроет ли функция файл так же, как это сделает with open
        tested = fileUtils.openJSON("../Reference_JSONs/Values.json", "r")
        with open("../Reference_JSONs/Values.json", "r") as file:
            reference = json.load(file)
        self.assertDictEqual(tested , reference)

    def test_openJSON_is_dict(self): # является ли открытый файл словарем, как нужно для выполнения задания
        with open("../Reference_JSONs/Values.json", "r") as file:
            opened = json.load(file)
        self.assertIsInstance(opened , dict)

    def test_openJSON_wrong_raise_exit(self): # поднимит ли функция ошибку, если на входе будет некорректный json
        with self.assertRaises(SystemExit) as cm:
            fileUtils.openJSON("../Test_JSONs/Wrong.json", "r")
        self.assertEqual(cm.exception.code, 0)


class TestCreateJSON(TestCase):

    def test_createJSON_make_dict(self): # пишет ли функция словарь
        prob = {"write": {"any": "thing"}} # данные, которые необходимо записать в файл
        fileUtils.createJSON(prob, "../Test_JSONs/Temp.json", 'w') # запишем данные, используя функцию createJSON
        with open("../Test_JSONs/Temp.json", "r") as file: # откроем "вручную" получившийся файл
            opened = json.load(file)
        self.assertIsInstance(opened , dict) # проверим, является ли содержимое словарем
        os.remove("../Test_JSONs/Temp.json") # и удалим чтобы не засорять папку

    def test_creatJSON_final_file_looks_like_reference(self): # проверим, является ли вывод нашей программы правильным и соответствующим корректному, данному в заданни
        with open("../Result_JSON/StructureWithValues.json", "r") as fileCreated: # откроем результат программы
            output = json.load(fileCreated)
        with open("../Reference_JSONs/StructureWithValues.json", "r") as fileRef: # откроем достоверный результат
            ref = json.load(fileRef)
        self.assertDictEqual(output , ref)
