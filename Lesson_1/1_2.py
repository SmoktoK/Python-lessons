"""
По введенным пользователем координатам двух точек вывести уравнение прямой
вида y=kx+b, проходящей через эти точки.
https://drive.google.com/file/d/1AWODciQ8VOinjZaI7TDYIg6Sf018-ib2/view?usp=sharing
"""


print('Координаты точки A(x1;y1):')
x1 = float(input('Введите x1: '))
y1 = float(input('Введите y1: '))

print('Координаты точки B(x2;y2):')
x2 = float(input('Введите x2: '))
y2 = float(input('Введите y2: '))

a = (y1 - y2) / (x1 - x2)
b = y2 - a * x2
print('Уравнение прямой, проходящей через эти точки:')
print(f'y = {a}*x + {b}')
