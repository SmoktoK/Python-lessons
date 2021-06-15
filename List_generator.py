from random import randint

size = 10
min_item = 0
max_item = 100
array = [randint(min_item, max_item) for _ in range(size)]
print(f'Изначальный массив данных: \n{array}')
