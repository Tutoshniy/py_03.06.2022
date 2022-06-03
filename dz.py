# Задание 1 Дан список чисел. Создать список, в который попадают числа, 
# описываемые возрастающую последовательность.

# nums = [3, 1, 2, 3, 4, 6, 1, 7]

# def get_up(nums):
#     next = [nums[0]]
#     for i in nums:
#         if i > max(next):
#             next.append(i)
#     return next
    
# print(get_up(nums))

# Задание 2 Создать и заполнить файл случайными целыми значениями. 
# Выполнить сортировку содержимого файла по возрастанию.

# from random import randint

# with open('file.txt','w') as data:
#     for i in range (randint(1,14)): 
#         data.write(str(randint(1,1000)) + ',')

# with open('file.txt','r') as data2:
#     a=data2.readline().split(',')
#     a.pop()
#     print(sorted(map(int, a)))

# Задание 3  найти триплеты и просто выводить их на экран. 
# Триплетом называются три числа, которые в сумме дают 0. 
# (решение будет долгим, ибо является демонстрационным при теме 
# многопоточного программирования).

from dataclasses import replace
from re import A


def findTriplets(arr, n):
    found = False
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if (arr[i] + arr[j] + arr[k] == 0):
                    print(arr[i], arr[j], arr[k])
                    found = True   
    if (found == False):
        print("Триплеты не найдены")
def concatenation(*params):
        res: str = ""
        for item in params:
            res+= item
        return res

chisla = []
with open('file.txt', 'r') as data:
    for line in data:
        line = concatenation(line)
        line.replace('\n','')
        line.replace(' ', '')
        chisla.append(int(line))
n = len(chisla)
findTriplets(chisla, n)