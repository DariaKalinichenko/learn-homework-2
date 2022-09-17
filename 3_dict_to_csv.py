"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv
from dataclasses import fields

users = [{'name': 'Daria', 'age': 24, 'job': 'backend developer'}, 
         {'name': 'Georgi', 'age': 54, 'job': 'developer'},
         {'name': 'Sonya', 'age': 33, 'job': 'HR'},
         {'name': 'Alex', 'age': 27, 'job': 'HR'}]

def main():
    with open('export.csv', 'w', encoding='utf-8') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for user in users:
            writer.writerow(user)

if __name__ == "__main__":
    main()
