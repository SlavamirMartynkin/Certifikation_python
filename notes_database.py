from notes_view import *

def write_name(name):
    with open("input.csv", "a", encoding="UTF-8") as file:
        file.write(name)

def serch_data():
    num = input_search_char()
    serch_char = input_char()
    with open("input.csv", "r", encoding="UTF-8") as file:
        lst = file.readlines()
        fnd_lst = []
        if num == 1:
            for row in lst:
                if row.split(';')[0] == serch_char:
                    fnd_lst.append(row)
        if num == 2:
            for row in lst:
                if row.split(';')[1] == serch_char:
                    fnd_lst.append(row)
        if num == 3:
            for row in lst:
                if row.split(';')[2] == serch_char:
                    fnd_lst.append(row)   
        return fnd_lst   
    
def serch_change_data():
    with open("input.csv", "r", encoding="UTF-8") as file:
        lst = file.readlines()
        print("Вы хотите изменить:")
        print(*serch_data())
        id = input('Введите id заметки: ')
        print('Введите новые данные: ')
        for i in range(len(lst)):
            if lst[i].split(',')[0] == id:
                lst[i] = input_name()
    with open("input.csv", "w", encoding="UTF-8") as file:
        for row in lst:
            file.write(row)

def serch_delete_data():
    with open("input.csv", "r", encoding="UTF-8") as file:
        lst = file.readlines()
        print("Вы хотите изменить:")
        print(*serch_data())
        id = input('Введите id заметки: ')
        print('Введите новые данные: ')
        for i in range(len(lst)):
            if lst[i].split(';')[0] == id:
                lst[i] = ''
    with open("input.csv", "w", encoding="UTF-8") as file:
        for row in lst:
            file.write(row)

def sort_data():
    with open("input.csv", "r", encoding="UTF-8") as file:
        lst = file.readlines()
        num = sort_char()
        if num == 1:
            lst.sort(key= lambda x: int(x.split(';')[0]))
        if num == 2:
            lst.sort(key= lambda x: x.split(';')[1])
        if num == 3:
            lst.sort(key= lambda x: x.split(';')[3])
    with open("input.csv", "w", encoding="UTF-8") as file:
        for row in lst:
            file.write(row)
            print(row)     

def all_list():
     with open("input.csv", "r", encoding="UTF-8") as file:
        lst = file.readlines()
        for row in lst:
            print(row)
