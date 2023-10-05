from notes_database import *
import datetime

def input_num():
    ask = int(input('Выберите действие: \n 1 - Новая заметка\n 2 - Найти заметку\n '
                    '3 - Найти и изменить заметку\n 4 - Найти и удалить заметку\n 5 - Удалить все\n '
                    '6 - Отсортировать по параметру\n 7 - Показать все заметки\n'))
    return ask

def input_name():
    id = '1'
    with open("input.csv", "r", encoding="UTF-8") as file:
        lst = file.readlines()
        lst.sort(key= lambda x: int(x.split(';')[0]))
        for row in lst:
            if row.split(';')[0] == id:
                id = str(int(id) + 1) 
    name = input('Введите заголовок: ')
    surname = input('Введите заметку: ')
    current_date_time = datetime.datetime.now()
    dt = current_date_time.strftime('%Y/%m/%d %H:%M:%S')
    res = id + ";" + name + ";" + surname + ";" + dt + '\n' 
    return res

def input_search_char():
    search_char = int(input('Выберите параметр поиска: \n 1 - id \n 2 - Заголовок \n 3 - Заметка \n'))
    return search_char

def input_char():
    char = input("Введите параметр:\n")
    return char

def sort_char():
    ask = int(input('Выберите параметр сортировки: \n 1 - id \n 2 - Заголовок \n 3 - Дата \n'))
    return ask