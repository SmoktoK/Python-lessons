"""
Проанализировать скорость и сложность одного любого алгоритма
из разработанных в рамках домашнего задания первых трех уроков.
"""

import math
import timeit
import cProfile

"""
Функция поиска i-го простого числа, без использования алгоритма «Решето Эратосфена»
"""


def sieve_without_eratosthenes(i):
    lst_prime = [2]
    number = 3
    while len(lst_prime) < i:
        flag = True
        for j in lst_prime.copy():
            if number % j == 0:
                flag = False
                break
        if flag:
            lst_prime.append(number)
        number += 1
    return lst_prime[-1]


"""
Функция поиска i-го простого числа, используя алгоритм «Решето Эратосфена»
"""


def sieve_eratosthenes(i):
    i_max = prime_counting_function(i)
    lst_prime = [_ for _ in range(2, i_max)]

    for number in lst_prime:
        if lst_prime.index(number) <= number - 1:
            for j in range(2, len(lst_prime)):
                if number * j in lst_prime[number:]:
                    lst_prime.remove(number * j)
        else:
            break
    return lst_prime[i - 1]


"""
Функция возвращает верхнюю границу отрезка на котором лежат
i-e количество простых чисел. Функция основана на теореме о
распределении простых чисел, она утверждает, что функция
распределения простых чисел. Количество простых чисел на отрезке
[1;n] растёт с увеличением n как n / ln(n).
"""


def prime_counting_function(i):
    number_of_primes = 0
    number = 2
    while number_of_primes <= i:
        number_of_primes = number / math.log(number)
        number += 1
    return number


NUMBER_EXECUTIONS = 1
TEST_VALUE = 1000

cProfile.run(f'sieve_without_eratosthenes({TEST_VALUE})')
cProfile.run(f'sieve_eratosthenes({TEST_VALUE})')
time1 = timeit.timeit(f'sieve_without_eratosthenes({TEST_VALUE})',
                      setup='from __main__ import sieve_without_eratosthenes',
                      number=NUMBER_EXECUTIONS)

time2 = timeit.timeit(f'sieve_eratosthenes({TEST_VALUE})',
                      setup='from __main__ import sieve_eratosthenes',
                      number=NUMBER_EXECUTIONS)

print(f'Программа без использования алгоритма «Решето Эратосфена» быстрее \
программы с использованием алгоритма «Решето Эратосфена» в \
{round(time2 / time1, 2)} раз')

"""
 Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.035    0.035 <string>:1(<module>)
        1    0.029    0.029    0.035    0.035 les_4_task_1.py:15(sieve_without_eratosthenes)
        1    0.000    0.000    0.035    0.035 {built-in method builtins.exec}
     7918    0.001    0.000    0.001    0.000 {built-in method builtins.len}
      999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
     7917    0.005    0.000    0.005    0.000 {method 'copy' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         19372 function calls in 2.749 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    2.749    2.749 <string>:1(<module>)
        1    2.596    2.596    2.749    2.749 les_4_task_1.py:35(sieve_eratosthenes)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:37(<listcomp>)
        1    0.002    0.002    0.003    0.003 les_4_task_1.py:58(prime_counting_function)
        1    0.000    0.000    2.749    2.749 {built-in method builtins.exec}
     1130    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     9118    0.001    0.000    0.001    0.000 {built-in method math.log}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1130    0.007    0.000    0.007    0.000 {method 'index' of 'list' objects}
     7988    0.143    0.000    0.143    0.000 {method 'remove' of 'list' objects}


Программа без использования алгоритма «Решето Эратосфена» быстрее программы с 
использованием алгоритма «Решето Эратосфена» в 86.1 раз
"""
