"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

result = {}
for i in range(2, 10):
    result[i] = []
    for num in range(2, 100):
        if num % i == 0:
            result[i].append(num)
    print(f'Для {i} кратных чисел: {len(result[i])}. Кратные числа: {result[i]}.')
