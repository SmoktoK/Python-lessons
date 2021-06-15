"""
В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""

from random import randint

size = 10
min_item = -100
max_item = 100
array = [randint(min_item, max_item) for _ in range(size)]
print(f'Изначальный массив данных: \n{array}')

ind = -1
i = 0
while i < size:
    if array[i] < 0 and ind == -1:
        ind = i
    elif 0 > array[i] > array[ind]:
        ind = i
    i += 1

print(f'Максимальный отрицательный элемент {array[ind]} находится на {ind+1} месте.')
