# Дан список, заполненный произвольными целыми числами.
# Примечание: для генерации списка используйте функцию.
# Найдите:
# 1. Количество элементов списка не превышающие 10
# 2. Сумму всех положительных элементов списка
# 3. Среднее арифметическое всех четных элементов
import random
numbers = []
n = 8
i = 0
while i < n:
    numbers.append(random.randint(-100, 100))
    i += 1

print(numbers)

lst1 = [num for num in numbers if num <= 10]
print(f'Кол-во элементов меньше 10:  {len(lst1)}')

lst2 = [num for num in numbers if num >0]
s2 = sum(lst2)
print(lst2, f'Сумма положительных элемнтов = {s2}')

lst3 = [num for num in numbers if num % 2 == 0]
s3 = sum(lst3)/len(lst3)
print(lst3, f'Среднее арифметическое = {s3}' )
