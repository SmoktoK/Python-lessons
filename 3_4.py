"""
Определить, какое число в массиве встречается чаще всего.
"""

from random import randint

size = 40
min_item = 0
max_item = 100
array = [randint(min_item, max_item) for _ in range(size)]
print(f'Изначальный массив данных: \n{array}')

num = None
max_frq = 1

for i in array:
    frq = 1
    for k in range(i + 1, size):
        if array[i] == array[k]:
            frq += 1
    if frq > max_frq:
        max_frq = frq
        num = array[i]
if max_frq > 1:
    print(f'Число {num} встречается {max_frq} раз(а)')
else:
    print('Все элементы уникальны')
