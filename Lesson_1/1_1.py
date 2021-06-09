"""
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь
https://drive.google.com/file/d/1AWODciQ8VOinjZaI7TDYIg6Sf018-ib2/view?usp=sharing
"""


my_num = int(input('Введите трехзначное число: '))
a = my_num // 100
print('Первое число: ', a)
b = my_num % 100 // 10
print('Второе число: ', b)
c = my_num % 10
print('Третье число: ', c)

num_sum = a + b + c
print('Сумма чисел равна: ', num_sum)
prod_num = a * b * c
print('Произведение чисел: ', prod_num)
