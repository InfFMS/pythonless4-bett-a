# Напишите функцию, которая «переворачивает» число,
# то есть возвращает число, в котором цифры стоят в обратном порядке.
# Вводится натуральное число
# Пользоваться input()[::-1] запрещено!
# Идея задачи реализовать алгоритм,
# который будет работать для любого введенного натурального числа.

def reverse_num(num):
    lst = []
    while num:
        q = num % 10
        lst.append(str(q))
        num //= 10

    new_num = ''.join(lst)
    return new_num

print(reverse_num(int(input())))
