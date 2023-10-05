from notes_database import *
from notes_view import *

def main():
    while True:
        num = input_num()
        if num == 1:
            res = input_name()
            write_name(res)
            print('Успешно записано\n')
        if num == 2:
            print(*serch_data(), sep= "; ")
            print('Успешно найдено\n')
        if num == 3:
            serch_change_data()
            print('Успешно изменено\n')
        if num == 4:
            serch_delete_data()
            print('Успешно удалено\n')
        if num == 5:
            with open("input.csv", "w", encoding="UTF-8") as file:
                file.write('')
            print('Список чист\n')
        if num == 6:
            sort_data()
            print('Успешно отсортировано')
        if num == 7:
            all_list()
main()
