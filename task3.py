# Напишите процедуру, которая выводит на экран
# запись переданного ей числа в римской системе счисления.
# Числа находятся в диапазоне [1, 3999]
# I - 1, V - 5, X - 10, L - 50, C  - 100, D - 500, M - 1000
# Пример:
# 2013
# MMXIII

dct = {1: 'I',
       4: 'IV',
       5: 'V',
       9: 'IX',
       10: 'X',
       40: 'XL',
       50: 'L',
       90: 'XC',
       100: 'C',
       400: 'CD',
       500: 'D',
       900: 'CM',
       1000: 'M'}
l = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
def rome_num(num):
    x = 0
    while num:
        per = l[x]
        while num - per >= 0:
            print(dct[per], end='')
            num -= per
        x += 1
'''
a = []
def rome_num(num):
    m = num // 1000
    a.append(m * 'M')
    num %= 1000
    if num // 100 == 9:
        a.append('CM')
    else:
        d = num // 500
        a.append(d * 'D')
    num %= 500
    c = num // 100
    if c == 4:
        a.append('CD')
    else:
        a.append(c * 'C')

    num %= 100
    if num // 10 == 9:
        a.append('XC')
    else:
        l = num // 50
        a.append(l * 'D')
    num %= 50

    if num // 10 == 4:
        a.append('XL')
    else:
        x = num // 10
        a.append(x * 'X')
    num %= 10

    if num == 9:
        a.append('IX')
    else:
        v = num // 5
        a.append(v * 'V')
    num %= 5

    if num == 4:
        a.append('IV')
    else:
        i = num // 1
        a.append(i * 'I')

    q = ''.join(a)
    return q
'''
rome_num(int(input()))