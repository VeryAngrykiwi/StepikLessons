n = int(input())
lst = [[1]]
for i in range(1, n + 1):
  row = [1] * (i + 1)
  for j in range(i + 1):
    if j != 0 and j != i:
      row[j] = lst[i - 1][j - 1] + lst[i - 1][j]
  lst.append(row)

print (lst[-1])

'''
def pascal(num):
  if num == 0:
      return [1]
  else:
      line = [1]
      prev_line = pascal(num - 1)
      for i in range(len(prev_line) - 1):
          line.append(prev_line[i] + prev_line[i + 1])
      line += [1]
  return line

num = int(input())
print(pascal(num))


def pascal(n):
  # начальная строка
  cur_seq = [1]

  for _ in range(n):
      # добавляем нули по бокам к текущей строке строке
      cur_seq = [0] + cur_seq + [0]
      # тут будет храниться новая строка
      new_seq = []

      for i in range(len(cur_seq) - 1):
          # добавляем в новую строку сумму соседних элементов текущей строки
          new_seq.append(cur_seq[i] + cur_seq[i + 1])

      # теперь новая строка становится нашей текущей строкой
      cur_seq = new_seq

  return cur_seq


n = int(input())
print(pascal(n))


"""------------ Классический вариант с построением всего треугольника ------------
a = [[1], [1, 1]]
b = int(input())
for i in range(b):
    c = []
    for j in range(0, len(a[-1]) - 1):
        c.append(a[-1][j] + a[-1][j + 1])
    c.insert(0, 1)
    c.append(1)
    a.append(c)
print(a[b])
-------------------------------------------------------------------------------"""
#---- Вариант с zip с нахождением последней строки без сохранения треугольника ---
a = [1]
for i in range(int(input())):
    a = [x + y for x, y in zip([*a, 0], [0, *a])]
print(a)


l = [1]
for _ in range(int(input())):
    l = [a + b for a, b in zip([*l, 0], [0, *l])]
print(l)


import math

n = int(input())
print([math.comb(n, k) for k in range(n + 1)])


num = int(input()) + 1
n = 1
lst = [1, 1]
lst1 = []
while n != num:
    for i in range(n-1):
        lst1.append(lst[i] + lst[i+1])
    lst1.append(1)
    lst1.insert(0, 1)
    lst = lst1.copy()
    lst1.clear()
    n += 1
print(lst if num > 1 else [1])


print((lambda n: [__import__('math').comb(n, k) for k in range(n+1)])(int(input())))
'''