import argparse #парсер аргументной коммандной строки
import json
from textwrap import indent
# TODO: читать файл конфига и выводить
# TODO: открывать файл и менять настройку(-и)
# TODO: написать документацию
# TODO: написать README


#чтение конфига
def read_config(filepath):
    with open(filepath,"r", encoding="utf-8") as f:
        data=json.load(f)
        print(data)
    return data
def main():
    parser= argparse.ArgumentParser(description="Работа с файлами конфигурации")
    #создание аргумента для выбора дейтсвия
    parser.add_argument("action", type=str ,choices=['read', 'write'])
    #создание аргумента для имени файла
    parser.add_argument("filepath", type=str)


    #парсинг и сохранение в args
    args=parser.parse_args()


    if args.action=="read":
        config_data=read_config(args.filepath)
        print(json.dumps(config_data, indent=2))
    elif args.action=="write":
        print("write")
    

if __name__ == "__main__":
    main()