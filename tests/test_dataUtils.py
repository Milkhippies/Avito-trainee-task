import utils.dataUtils as dataUtils
from unittest import TestCase
import pytest
import json


class TestReturnDictValueByKey(TestCase):
    
    def test_returnDictValueByKey_general(self): # отработает ли функция так же как простой .get
        stock = {'first': 'pervyi'}
        nonFunc = stock.get('first')
        func = dataUtils.returnDictValueByKey(stock, 'first')
        self.assertEqual(nonFunc , func)


class TestTransformListDictsToDict(TestCase):

    def test_transformListDictsToDict_is_dict(self): # получится ли на выходе словарь
        testData = [{'id': 1, 'value': 25}, {'id': 2, 'value': 52}, {'id': 6, 'value': 15}, {'id': 14, 'value': 1}]
        testData = dataUtils.transformListDictsToDict(testData, 'id', 'value')
        self.assertIsInstance(testData , dict)

    def test_transformListDictsToDict_general(self): # сработает ли программа так, как задумывали на тестовых данных
        testData = [{'id': 1, 'value': 25}, {'id': 2, 'value': 52}, {'id': 6, 'value': 15}, {'id': 14, 'value': 1}] 
        testDict = dataUtils.transformListDictsToDict(testData, 'id', 'value')
        ref = {1 : 25, 2 : 52, 6 : 15, 14 : 1}
        self.assertDictEqual(testDict , ref)


class TestSwapTitle(TestCase):

    def test_swapTitle_general(self): # сработает ли программа так, как задумывали на тестовых данные
        with open("../Test_JSONs/valuesDictAfterGetParam.json", "r") as file: # загрузим подготовленый словарь вида {'id':*id*, 'value' = *value*}
            valuesDict = json.load(file)
        with open("../Test_JSONs/valuesDictAfterSwapTitle.json", "r") as file: # загрузим достоверно посчитанный результат - словарь вида *id*:*value*
            result = json.load(file)
        with open("../Test_JSONs/dataAfterGetParam.json", "r") as file: # загрузим подготовленные данные для работы со словарем
            data = json.load(file)
        dataUtils.setParam(data, "id", dataUtils.swapTitle, valuesDict) # в результате получится словарь вида *id*:*title*, если удалось найти нужный id и title
        self.assertDictEqual(result , valuesDict)


class TestSwapValue(TestCase):

    def test_swapValue_general(self):
        with open("../Test_JSONs/valuesDictAfterSwapTitleArray.json", "r") as file: # загрузим массив словарей
            arrayValues = json.load(file)
        valuesDict = {}
        for i in range(len(arrayValues)):
            valuesDict.update({arrayValues[i][0] : arrayValues[i][1]}) # сделаем из массива словарей словарь
        with open("../Test_JSONs/dataAfterSwapValue.json", "r") as file: # загрузим достоверно посчитанный результат
            result = json.load(file)
        with open("../Test_JSONs/dataAfterGetParam.json", "r") as file: # загрузим рабочие данные
            data = json.load(file)
        dataUtils.setParam(data, "id", dataUtils.swapValue, valuesDict) # в результате будут заполнены поля 'value' значения соответствующими из словаря *id*:*value* для соответствующих id
        self.assertDictEqual(result , data)


@pytest.mark.parametrize( 
"test_input,expected",
    [
        pytest.param(14, 1, id= "value: 14 id: 1," ),
        pytest.param(-15, 2, id= "value: -15 id: 2" ),
        pytest.param('eg', 3, id= "value: eg id: 3" ),
        pytest.param(123, 'abc', id= "value: 123 id: abc" ),
        pytest.param('', 812, id= "value: '' id: 812" ),
    ],
)
def test_getKey_general(test_input, expected): #test_input == value, expected == key прогоним данные и посмотрим "функция(вход) == ожидаемый выход"
    testData = {1: 14, 2: -15, 3: 'eg', 'abc': 123, 812: ''}
    assert dataUtils.returnKeyByValue(testData, test_input) == expected

