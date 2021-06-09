"""
Определить, является ли год, который ввел пользователем, високосным или невисокосным
https://drive.google.com/file/d/1AWODciQ8VOinjZaI7TDYIg6Sf018-ib2/view?usp=sharing
"""
from calendar import isleap
year = int(input('Введите год: '))
if isleap(year) is True:
    print('Высокосный год')
else:
    print('Обычный год')
