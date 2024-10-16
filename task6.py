# Напишите функцию, которая сокращает дробь вида M/N.
# Где M и N - наутральные числа.
# В качестве аргументов она принимает числитель и знаменатель,
# выводит числитель и знаменатель после сокращения
#
# Пример:
# Ввод:
# 25 15
# Вывод:
# 5 3

def find(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1
    nod = 1
    for i in range(2, num1 + 1):
        if num1 % i == 0 and num2 % i == 0:
            nod = i

    return nod

def cut(a, b):
    n = find(a, b)
    a //= n
    b //= n
    return a, b

i, j = map(int, input().split())
print(*cut(i, j))
