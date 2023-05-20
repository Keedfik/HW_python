# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
'''
number = 0
while number > 1000 or number < 99:
    number = int(input("Input three-digit number: "))

print(f"{number//100} + {number//10%10} + {number%10} = {number//100 + number//10%10 + number%10}")
'''
# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал
# каждый ребенок, если известно, что Петя и Сережа сделали
# одинаковое количество журавликов, а Катя сделала в два раза
# больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
'''
summ = int(input("Amount of cranes: "))

if summ%6 == 0:
    print(f"Petya and Serezha made {summ//6} cranes each and Katya made {(summ//6)*4} cranes")
else:
    print("That can't be")
'''
# Задача 6: Вы пользуетесь общественным транспортом? Вероятно,
# вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no
'''
number = 0
while number > 1000000 or number < 99999:
    number = int(input("Input six-digit number: "))

left = number//100000 + number // 10000 % 10 + number//1000 % 10
right = number % 10 + number % 100 // 10 + number % 1000 // 100

if left == right:
    print("You have a lucky ticket :)")
else:
    print("This ticket is unlucky :(")
'''
# Задача 8: Требуется определить, можно ли от шоколадки размером
# n × m долек отломить k долек, если разрешается сделать один
# разлом по прямой между дольками (то есть разломить шоколадку
# на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

rows = int(input("Input rows: "))
cols = int(input("Input cols: "))
piece = int(input("Input amount of pieces: "))

if piece < rows * cols and ((piece % rows == 0) or (piece % cols == 0)): 
    print("Yes")
else:
    print("No")