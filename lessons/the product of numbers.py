s = [int(input()) for _ in range(int(input()))]
k = int(input())
flag = False
for i in range(len(s)):
  for q in range(len(s)):
    if s[i] * s[q] == k and i != q:
      flag = True
      break
if flag:
  print('ДА')
else:
  print('НЕТ')

'''
numbers, multiply = [int(input()) for i in range(int(input()))], int(input())
for i in range(len(numbers)-1):
    for j in range(i+1, len(numbers)):
        if multiply == numbers[i] * numbers[j]:
            exit(print("ДА"))
print("НЕТ")

from itertools import combinations
numbers = [int(input()) for _ in range(int(input()))]
target = int(input())

print('ДА' if len([1 for a, b in combinations(numbers, 2) if a * b == target]) else 'НЕТ')

s, product = [int(input()) for _ in range(int(input()))], int(input())
print('ДА' if any([s[i] * j == product for i in range(len(s)) for j in s[i+1:]]) == 1 else 'НЕТ')

import itertools

total = int(input())
numbers = [int(input()) for _ in range(total)]
sum = int(input())

for a, b in itertools.combinations(numbers, 2):
    if a * b == sum:
        print("ДА")
        break
else:
    print("НЕТ")


size = int(input())
seq = [int(input()) for _ in range(size)]
number = int(input())
flag = False

for i in range(size):
    for j in range(size):
        if i != j and seq[i] * seq[j] == number:
            flag = True

if flag:
    print("ДА")
else:
    print("НЕТ")


# Считываем количество чисел в наборе
n = int(input())

# Считываем набор чисел
numbers = []
for _ in range(n):
    numbers.append(int(input()))

# Считываем целевое число
target = int(input())

# Инициализируем переменную для хранения результата
result = "НЕТ"

# Проверяем, является ли число произведением двух чисел из набора
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i != j and numbers[i] * numbers[j] == target:
            result = "ДА"
            break

# Выводим результат
print(result)

print("ДА" if (mas := [int(input()) for _ in range(int(input()) + 1)])[-1] in [mas[ind0] *mas[ind] for ind in range(len(mas) - 1) for ind0 in range(len(mas) - 1) if ind != ind0] else "НЕТ")

'''
