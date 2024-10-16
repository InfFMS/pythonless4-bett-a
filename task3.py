# Напишите процедуру, которая выводит на экран
# запись переданного ей числа в римской системе счисления.
# Числа находятся в диапазоне [1, 3999]
# I - 1, V - 5, X - 10, L - 50, C  - 100, D - 500, M - 1000
# Пример:
# 2013
# MMXIII

def rome_num(num):
    m = num // 1000
    num %= 1000
    d = num // 500
    num %= 500
    c = num // 100
    num %= 100
    l = num // 50
    num %= 50
    x = num // 10
    num %= 10
    v = num // 5
    num %= 5
    i = num // 1
    print(m * 'M' + d * 'D' + c * 'C' + l * 'L' + x * 'X' + v * 'V' + i * 'I')

rome_num(int(input()))