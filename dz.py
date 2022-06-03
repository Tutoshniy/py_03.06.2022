# Задание 1 Дан список чисел. Создать список, в который попадают числа, 
# описываемые возрастающую последовательность.

nums = [3, 1, 2, 3, 4, 6, 1, 7]

# Первый вариант

def get_up(nums):
    next = [nums[0]]
    for i in nums:
        if i > max(next):
            next.append(i)
    return next
    
print(get_up(nums))