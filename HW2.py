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

if count_tails<count_heads:
    flips = count_tails
else: 
    flips = count_heads

print(f"Min number of coins = {flips}")
'''
# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму 
# этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.



# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.

number = 0
while number <= 0:
    number = int(input("Input number: "))

power = 2
print(power)

for i in range(number-1):
    power *= 2
    print(power)
