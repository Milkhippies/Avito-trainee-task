import json
import sys

def createErrorJSON(way, arg):
    with open(way, arg) as file: # пишем новый JSON для Error
        json.dump({"error": {"message": "Входные файлы некорректны"}}, file, indent=4, ensure_ascii=False) # отступ 4, ensure_ascii=False чтобы кириллица была читаема при просмотре
    print('error.json was created \n')
    sys.exit(0)

def openJSON(way, arg):
    with open(way, arg) as file: # открываем файл 
        try:
            opened = json.load(file) # записываем содержимое файла
        except ValueError:
            print(way + ' is bad \n') # если JSON неконсистентный то отлавливаем ошибку и вызываем makeError
            createErrorJSON("../Result_JSON/error.json","w")
        else:
            print(way + ' is good \n') # если JSON в порядке, то возвращаем содержимое
            return opened

def createJSON(data, way, flag):
    with open(way, flag) as file: # пишем новый JSON
        json.dump(data, file, indent=3, ensure_ascii=False) # отступ 4, ensure_ascii=False чтобы кириллица была читаема при просмотре
    print(way + ' was created\n')

