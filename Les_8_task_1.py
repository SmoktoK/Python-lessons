"""
Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
"""

import hashlib

stroke = input('Введите строку: ')
count_array = []


def mycount(str_):
    str_hash = hashlib.sha256(str_.encode('utf-8')).hexdigest()
    if len(str_) % 2 == 0 and len(str_) == 2:
        a = hashlib.sha256(str_[0].encode('utf-8')).hexdigest()
        b = hashlib.sha256(str_[1].encode('utf-8')).hexdigest()
        c = hashlib.sha256((str_[0] + str_[1]) .encode('utf-8')).hexdigest()
        if a not in count_array:
            count_array.append(a)
        if b not in count_array:
            count_array.append(b)
        if c not in count_array:
            count_array.append(c)
        if str_hash in count_array:
            count_array.remove(str_hash)
        return f'Количество подстрок в слове "{stroke}" составляет {len(count_array)}'

    if len(str_) % 2 != 0 and len(str_) == 1:
        a = hashlib.sha256(str_[0].encode('utf-8')).hexdigest()
        if a not in count_array:
            count_array.append(a)
        if str_hash in count_array:
            count_array.remove(str_hash)
        return f'Количество подстрок в слове "{stroke}" составляет {len(count_array)}'

    n = 0
    while len(str_) > n:
        result = ''
        for i in range(n, len(str_)):
            result = (result + str_[i])
            hash_ = hashlib.sha256(result.encode('utf-8')).hexdigest()
            if hash_ not in count_array:
                count_array.append(hash_)
        n += 1
    else:
        str_ = str_[1:-1]  # отсекаю строку, т.к. хэши двух крайних символов я учел предыдущем пробеге по строке
    return mycount(str_)


print(mycount(stroke))
