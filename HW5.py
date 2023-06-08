# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# Пример:
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 
'''
def power_number(a, b):
    if b == 0:
        return 1
    if b < 0:
        return power_number(a, b + 1) * 1 / a
    return power_number(a, b - 1) * a

print(power_number(int(input("Input first number: ")), int(input("Input power number: "))))
'''

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух
#  целых неотрицательных чисел. Из всех арифметических операций допускаются 
#  только +1 и -1. Также нельзя использовать циклы.
# Пример:
# 2 2
#     4 

def summa(a, b):
    if b < 0 < a:
        a, b = b, a 
    if b == 0:
        return a
    return summa(a + 1, b - 1)

# n = -1
# while n <0:
n = int(input("Input first number: "))

# m = -1
# while m <0:
m = int(input("Input second number: "))

print(summa(n, m))
