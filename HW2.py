# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно 
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
'''
coins = 0
while coins <= 0:
    coins = int(input("Input number of coins: "))

count_heads = 0
count_tails = 0 

print("1 - heads, 0 - tails")

for i in range(coins):
    side = int(input(f"Input {i+1} coin side: ")) #heads-орел tails-решка
    if side == 0:
        count_tails += 1
    else:
        count_heads += 1

print(f"Min number of coins = {min(count_heads, count_tails)}")
'''

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму 
# этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
'''
summ = 0
while summ <= 0:
    summ = int(input("Input sum numbers: "))
product = 0
while product <= 0:
    product = int(input("Input product of numbers: "))
flag = True
for i in range(summ):
    for j in range(product):
        if i + j == summ and i*j == product and flag:
            print(f"first number = {i}, second number = {j}")
            flag = False
if flag == True:
    print("Doesn't exist")
'''
# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.
'''
number = -1
while number < 0:
    number = int(input("Input number: "))

power = 0

while 2**power <= number:
    print(2**power)
    power +=1
'''