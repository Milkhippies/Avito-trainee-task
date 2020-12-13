import utils.dataUtils as dataUtils
import utils.fileUtils as fileUtils

print('Try open Values.json \n')

values = fileUtils.openJSON("Reference_JSONs/Values.json", "r")
values = dataUtils.returnDictValueByKey(values, 'values')

    # {'id': ***, 'value': ***} массив словарей 
    # value[0]= {id:34, value: 298}

valuesDict = dataUtils.transformListDictsToDict(values,"id","value") # делаем из массива словарей один словарь

    # {34 : 298, 146 : 'Валидация...', 73 : 345, ...}

print('Try open TestcaseStructure.json \n')

data = fileUtils.openJSON("Reference_JSONs/TestcaseStructure.json", "r")

    # {'id': num ,'title': 'str', 'value': ''} массив параметров
    # data[0]= {'id': 34 ,'title': 'testcaseId', 'value': ''} 
    # data[1]= {'id': 146 ,'title': 'Testcase name', 'value': ''} 

dataUtils.setParam(data, "id", dataUtils.swapTitle, valuesDict)
dataUtils.setParam(data, "id", dataUtils.swapValue, valuesDict)
fileUtils.createJSON(data,"Result_JSON/StructureWithValues.json", "w")