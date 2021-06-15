"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random

size = 10
min_item = 0
max_item = 100
array = [random.randint(min_item, max_item) for _ in range(size)]
print(f'Изначальный массив данных: \n{array}')
max_num = array[size-1]
min_num = array[0]
# print(min_num, max_num)

for i in array:
    if i > max_num:
        max_num = i
    if i < min_num:
        min_num = i
print('Минимальное число: ', min_num)
print('Максимальное число', max_num)

min_index = array.index(min_num)
max_index = array.index(max_num)
array[min_index], array[max_index] = array[max_index], array[min_index]
print(f'Массив после замены местами элементов {min_num} и {max_num}: \n{array}')


