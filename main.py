import argparse #парсер аргументной коммандной строки 
import json 
from textwrap import indent 

#изменение параметра в конфиге 
def update_config(config, param, value): 
    keys=param.split(".") #путь к параметру 
    for key in keys[:-1]: #проходим по всем ключам кроме последнего 
        #проходим к след уровню сложности, если ключа нет, то создаем пустой словарь 
        config = config.setdefault(key, {})
    config[keys[-1]] = value #устанавливаем новое значение для последнего ключа
 
def write_config(filepath, config): 
    with open(filepath, "w", encoding="utf-8") as f: 
        json.dump(config, f, indent=4) 
 
#чтение конфига 
def read_config(filepath): 
    with open(filepath, "r", encoding="utf-8") as f: 
        data = json.load(f) 
    return data 

def main(): 
    parser = argparse.ArgumentParser(description="Работа с файлами конфигурации") 
    #создание аргумента для выбора действия 
    parser.add_argument("action", type=str, choices=['read', 'write'], help="Действие которое надо выполнить: read или write") 
    #создание аргумента для имени файла 
    parser.add_argument("filepath", type=str, help="Путь к файлу конфигурации") 
    #создание аргумента для параметра и его нового значения 
    parser.add_argument("--param", type=str, help="Параметр и значение для этого параметра в формате: key=value (только для действия write)") 
 
    #парсинг и сохранение в args 
    args = parser.parse_args() 
    if args.action == "read": 
        config_data = read_config(args.filepath) 
        print(json.dumps(config_data, indent=2)) 
        print("Содержимое конфига:") 
    elif args.action == "write": 
        config_data = read_config(args.filepath) # Чтение конфига перед записью
        path, value = args.param.split("=") 
        update_config(config_data, path, value) 
        write_config(args.filepath, config_data) 
        print("Конфигурация обновлена") 

if __name__ == "__main__": 
    main()
