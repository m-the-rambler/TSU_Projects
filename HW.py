# Напишите функцию, которая получает на вход массив строк и удаляет из него все строки, в которых нет как минимум двух букв русского алфавита. Две одинаковые буквы тоже считаются: например, функция не должна удалять строку «бб».
import re

def remove_trash_strings(string_list):
    for i in range(len(string_list)):
        match_list = re.findall(r'[а-яёА-ЯЁ]', string_list[i])  # !!!
        if len(match_list) < 2:  # !!!
            string_list[i] = 'deleteme'  # !!!
    while 'deleteme' in string_list:
        string_list.remove('deleteme')  # !!!
    return string_list

string_list = ['', 'bb', 'бб', 'qwerty123',
    'абырвалг', 'а!!2']  # !!!

print(remove_trash_strings(string_list))