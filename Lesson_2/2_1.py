"""
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
https://drive.google.com/file/d/1ObiXYxii8Y_wxDSMySUnztvDFOjxi8vM/view?usp=sharing
"""

tot = number = int(input('Введите число: '))
even = 0
odd = 0
while number > 0:
    if number % 2 == 0:
        even += 1
    else:
        odd += 1
    number = number//10
print(f'в числе {tot}: {even} четных  и {odd} нечетных чисел')
