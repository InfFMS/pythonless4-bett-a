# Напишите функцию, которая находит
# наибольший общий делитель двух натуральных чисел
# На входе два числа, на выходе их НОД.

def find(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1
    nod = 1
    for i in range(2, num1 + 1):
        if num1 % i == 0 and num2 % i == 0:
            nod = i

    return nod

print(find(int(input()), int(input())))


