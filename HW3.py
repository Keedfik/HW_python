# Задача 16: Требуется вычислить, сколько раз встречается некоторое 
# число X в массиве A[1..N]. Пользователь в первой строке вводит 
# натуральное число N – количество элементов в массиве. В последующих  
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# Пример:
# 5
#     1 2 3 4 5
#     3
#     -> 1
'''
import random
print("\033c")

list_length = 0
while list_length <= 0:
    list_length = int(input("Input list's length "))

num_list = []

for i in range (list_length):
    num_list.append(random.randint(1, list_length))

print(num_list)

number = int(input("What number are we looking for? "))
print(f"Number {number} appears {num_list.count(number)} times")
'''

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине 
# элемент к заданному числу X. Пользователь в первой строке вводит 
# натуральное число N – количество элементов в массиве. В последующих  
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# Пример:
# 5
#     1 2 3 4 5
#     6
#     -> 5
'''
import random
print("\033c")

list_length = 0
while list_length <= 0:
    list_length = int(input("Input list's length "))

number = int(input("What number are we looking for? "))
num_list = []

for i in range (list_length):
    num_list.append(random.randint(1, list_length))

closest_num = num_list[0]

for i in range (list_length):
    if abs(number - closest_num) > abs(number - num_list[i]) :
        closest_num = num_list[i]
    
print(num_list)
print(f"Closest number to {number} in list is {closest_num}")
'''
# Задача 20:  В настольной игре Скрабл (Scrabble) каждая буква имеет 
# определенную ценность. В случае с английским алфавитом очки 
# распределяются так: 
# A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; 
# B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка; 
# K – 5 очков; 
# J, X – 8 очков; 
# Q, Z – 10 очков. 
# А русские буквы оцениваются так: 
# А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; 
# Й, Ы – 4 очка; 
# Ж, З, Х, Ц, Ч – 5 очков; 
# Ш, Э, Ю – 8 очков; 
# Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного
# пользователем слова. Будем считать, что на вход подается только одно слово, 
# которое содержит либо только английские, либо только русские буквы.
# Пример:
# ноутбук
#     12
'''
print("\033c")

d = {   1: ["A", "E", "I", "O", "U", "L", "N", "S", "T", "R",
        "А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"],
        2:["D", "G", "Д", "К", "Л", "М", "П", "У"],
        3:["B", "C", "M", "P", "Б", "Г", "Ё", "Ь", "Я"],
        4:["F", "H", "V", "W", "Y", "Й", "Ы"],
        5:["K", "Ж", "З", "Х", "Ц", "Ч" ],
        8:["J", "X", "Ш", "Э", "Ю"],
        10:["Q", "Z", "Ф", "Щ", "Ъ"]     
     }

word = input("Input word: ").upper()
score = 0 

for letter in word:
    for key, value in d.items():
        if letter in value:
            score += key

print(f"Your score: {score}")
'''