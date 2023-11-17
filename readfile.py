def my_cook_book():
    with open('cook.txt', encoding='utf-8') as file:
        cook_book = {}
        for line in file.read().split('\n\n'):
            name, _, *args = line.split('\n')
            cook_li = []
            for arg in args:
                ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, arg.split(' | '))
                cook_li.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cook_book[name] = cook_li
    return cook_book

def get_shop_list_by_dishes(dishes,person_count):
    new_cook = {}
    cook_book = my_cook_book()
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient['quantity'] *= person_count
                new_cook.setdefault(ingredient['ingredient_name'], ingredient)
   
    dic_dish = {}
    for value in new_cook.values():
        name = value['ingredient_name']
        del value['ingredient_name']
        dic_dish[name] = value
    print(dic_dish)
        
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'],2)

import os
import os.path

def strings_count(file):
    with open(file, 'r', encoding= 'utf-8') as f:
        return sum(1 for line in f)
    
base_path = os.getcwd()
location = os.path.abspath('D:/Мои документы/Илья/Обучение/Нетология/Python/домашние работы/homeworks/hw_readfile/files')
file_for_write = os.path.abspath('D:/Мои документы/Илья/Обучение/Нетология/Python/домашние работы/homeworks/hw_readfile/123.txt')
full_path = os.path.join(base_path, location)
def rewrite(full_path, file_for_write):
    files = []
    for i in list(os.listdir(full_path)):
        files.append([strings_count(os.path.join(full_path, i)), os.path.join(base_path, location, i), i])
    for file_item in sorted(files):
        opening_files = open(file_for_write, 'a', encoding= 'utf-8')
        opening_files.write(f'{file_item[2]}\n')
        opening_files.write(f'{file_item[0]}\n')
        with open(file_item[1], 'r', encoding= 'utf-8') as file:
            counting = 1
            for line in file:
                opening_files.write(f'строка № {counting} в файле {file_item[2]} : {line}')
                counting += 1
        opening_files.write(f'\n')
        opening_files.close()
rewrite(full_path, file_for_write)