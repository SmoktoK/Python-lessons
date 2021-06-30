"""
Посчитать, сколько раз встречается определенная цифра в введенной
последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать,
задаются вводом с клавиатуры.
"""
from sys import getsizeof as getsize

BASE = 10
sum_ = 0
num = int(input('Введите количество чисел: '))
digit = int(input('Какую цифру подсчитать: '))
count = 0
for i in range(1, num + 1):
    ans = int(input(f'Введите число {i}: '))
    while ans > 0:
        if ans % BASE == digit:
            count += 1
        ans //= BASE  # ans = ans // 10

sum_ += getsize(BASE)
sum_ += getsize(num)
sum_ += getsize(digit)
sum_ += getsize(count)
sum_ += getsize(ans)
print(f'Было введено {count} цифр(ы) {digit}')
print(sum_)


# sum_ = 0
# count = 0
# inp_0 = str(input('Введите последовательность :'))
# inp_0 = list(inp_0)
# inp_1 = str(input('Какой символ  будем искать?'))
#
# for i in inp_0:
#     if i == str(inp_1):
#         count += 1
# # print(getsize(count))
# sum_ += getsize(count)
# # print(getsize(inp_0))
# sum_ += getsize(inp_0)
# # print(getsize(inp_1))
# sum_ += getsize(inp_1)
# print(f'{count} раз(а) встречается число: {inp_1}')
# print(sum_)
