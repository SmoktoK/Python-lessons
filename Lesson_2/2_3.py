"""
Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
 Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
 https://drive.google.com/file/d/1ObiXYxii8Y_wxDSMySUnztvDFOjxi8vM/view?usp=sharing
"""

str_len = 1
for i in range(32, 128):
    if str_len % 10 == 0:
        print(f'{i:5}: {chr(i)}')
    else:
        print(f'{i:5}: {chr(i)}', end=' ')
    str_len += 1
