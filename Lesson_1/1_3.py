"""
Вводятся три разных числа.
Найти, какое из них является средним (больше одного, но меньше другого).
https://drive.google.com/file/d/1AWODciQ8VOinjZaI7TDYIg6Sf018-ib2/view?usp=sharing
"""


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
sum_num = a + b + c
max_num = a
min_num = c
if max_num < b:
    max_num = b
if max_num < c:
    max_num = c
if min_num > b:
    min_num = b
if min_num > a:
    min_num = a
tot_num = sum_num - max_num - min_num
print(f'Среднее число : {tot_num}')
