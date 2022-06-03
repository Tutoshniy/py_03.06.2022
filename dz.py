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

from random import randint

with open('file.txt','w') as data:
    for i in range (randint(1,14)): 
        data.write(str(randint(1,1000)) + ',')

with open('file.txt','r') as data2:
    a=data2.readline().split(',')
    a.pop()
    print(sorted(map(int, a)))