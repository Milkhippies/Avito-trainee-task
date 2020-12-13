import sys


def returnDictValueByKey(dict, value): #если неверный параметр value, то вернет None
    try:
        temp = dict.get(value)
    except AttributeError:
        print('В функцию returnDictValueByKey() следует передать словарь')
        sys.exit(0)
    else:
        return temp


def transformListDictsToDict(list, key, value): # делает из массива словарей новый словарь 
    newDict = {}
    for item in list:
        tempKey = item.get(key) # получаем значение словаря по ключу key (key : 17 -> 17)
        tempValue = item.get(value) # получаем значение словаря по ключу value (value : "some" -> "some")
        newDict.update({tempKey : tempValue})
    return newDict


def returnKeyByValue(dict, value):  # функция нахождения ключа словаря по значению:
    for index in dict:
        if dict[index] == value:
            return(index)
            break
    return(None)


def swapTitle(json, key, dict):     # функция для setParam - формируем рабочий словарь: 
    if json[key] in dict.values(): # если ключ совпадает с ключом из json value ->
        foundKey = returnKeyByValue(dict,json[key])
        dict.update({foundKey: json['title']}) # меняем значение по ключу в рабочем словаре на искомый title. Было "id: 73, value: 345" стало "id: 73, value: SellerX" 
    

    # тут будем искать ид, сравнивать его с идом в рабочем словаре и если есть совпадение - менять value параметра на соответствующий из рабочего словаря

def swapValue(json, key, dict): # функция для setParam - задаем value в json при совпадение id(key) в json и dict
    if json[key] in dict: 
        json['value'] = dict[json[key]]


def setParam(myjson, key, func, currentDict):
    if type(myjson) is dict:
        for jsonkey in (myjson):
            if type(myjson[jsonkey]) in (list, dict):
                setParam(myjson[jsonkey], key, func, currentDict)
            elif jsonkey == key:
                func(myjson, jsonkey, currentDict)
                #if func == 'swapTitle':
                #    swapTitle(myjson, jsonkey, valuesDict)
                #elif func == 'swapValue':
                #    swapValue(myjson, jsonkey, valuesDict)
    elif type(myjson) is list:
        for item in myjson:
            if type(item) in (list, dict):
                setParam(item, key, func, currentDict)
