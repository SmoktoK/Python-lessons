"""
Посчитать, сколько раз встречается определенная цифра во введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
https://drive.google.com/file/d/1ObiXYxii8Y_wxDSMySUnztvDFOjxi8vM/view?usp=sharing
"""

user_range = input('Введите последовательность цифр: ')
num = input('Введите цифру для поиска: ')
count = 0

for i in user_range:
    if i == num:
        count += 1

print(f'Цифра {num} встречается {count} раз(а)')
