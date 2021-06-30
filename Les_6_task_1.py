# 64-разрядная ОС / Python 3.9.0
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
import sys

# Способ №1
number = int(input("Введите целое трёхзначное число: "))
num_1 = number % 10
num_2 = (number % 100) // 10
num_3 = number // 100
sum_ = num_1 + num_2 + num_3
mult_ = num_1 * num_2 * num_3
print(f"Сумма цифр введённого Вами числа - {sum_}")
print(f"Произведение цифр введённого Вами числа - {mult_}")

count = [num_1, num_2, num_3, sum_, mult_]  # самый "топорный" вариант в плане решения задачи и подсчета результата:


# просто сумма из 5-ти вычисляемых значений, которая определяется путем "пробежки" по циклу и суммированию в переменную.

def show(x):
    result = sys.getsizeof(x)
    return result


total = 0
for i in count:
    total += show(i)

print(f'Сумма по всем объектам {total}')
# Сумма равняется 140. Пять раз взяли по 28.
