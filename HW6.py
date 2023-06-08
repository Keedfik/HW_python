# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
'''
print("\033c")

num = int(input("Input first number: "))
diff = int(input("Input difference: "))

list_length = 0
while list_length <= 0:
    list_length = int(input("Input list's length "))
list_num =[]
for i in range(list_length):
    list_num.append(num+i*diff)
print(list_num)
'''
# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Диапазон 5, 15

print("\033c")

numbers = [int(i) for i in input("Input numbers: ").split()]
for i in range(len(numbers)):
    if 4<numbers[i]<16:
        print(i, end=' ')