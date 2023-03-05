# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
#(т.е. не меньше заданного минимума и не больше заданного максимума)

import random
lst = []
quantity  = int (input ('Сколько элементов в массиве? '))
min_num = int(input('Введите минимальное значение диапозона: '))
max_num = int(input('Введите максимальное значение диапозона: '))
for i in range(quantity):
    lst.append(random.randint(-100, 100))
print (lst)
for i in range(len(lst)):
    if min_num <= lst[i] <= max_num:
        print(i, end = ' ')
    else:
        print ('Ни один элемент массива не входит в диапозон')