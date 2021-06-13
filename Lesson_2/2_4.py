"""
В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, вывести правильный ответ.
https://drive.google.com/file/d/1ObiXYxii8Y_wxDSMySUnztvDFOjxi8vM/view?usp=sharing
"""

from random import randint

x = 0
a = randint(1, 100)


def rand_num(a, x=1):
    b = int(input('Введите число от 1 до 100: '))
    if b == a:
        return print('Вы угадали!')
    if x == 10:
        return print('Вы проиграли!')
    if b > a:
        print("Загаданное число меньше!")
    if b < a:
        print('Загаданное число больше!')
    print(f'Осталось {10 - x} попыток')
    return rand_num(a, x + 1)


rand_num(a)
print('Это число: ', str(a))
