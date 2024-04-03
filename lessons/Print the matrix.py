#Вывести матрицу 1

# Taking input for number of rows and columns
n, m = int(input()), int(input())

# Creating an empty matrix to store elements
matrix = []

# Populating the matrix with input elements
for _ in range(n):
    row = [input() for _ in range(m)]
    matrix.append(row)

# Printing the matrix
for row in matrix:
    print(*row)

'''
n, m = int(input()), int(input())
matrix = []

for i in range(n):
  row = []
  for q in range(m):
    row.append(input())
  matrix.append(row)

for t in range(n):
  for k in range(m):
    print(matrix[t][k], end = ' ')
  print()
  

n, m = int(input()), int(input())
matrix = [[input() for _ in range(m)] for _ in range(n)]

for row in matrix:
    print(*row)


n = int(input())
m = int(input())

[print(*[input() for i in range(m)]) for i in range(n)]


n, m = int(input()), int(input())
a = [[input() for i in range(m)] for j in range(n)]
for x in a:
    print(*x)
'''


#Вывести матрицу 2
n, m = int(input()), int(input())
matrix = []

for i in range(n):
  row = []
  for q in range(m):
    row.append(input())
  matrix.append(row)

for t in range(n):
  for k in range(m):
    print(matrix[t][k], end = ' ')
  print()
print()
for g in range(m):
  for r in range(n):
    print(matrix[r][g], end = ' ')
  print()

'''
n, m = int(input()), int(input())
arr = [[input() for _ in range(m)] for _ in range(n)]
for row in arr:
    print(*row)
print()
for i in range(m):
    for j in range(n):
        print(arr[j][i], end=' ')
    print()

n, m = int(input()), int(input())
w = [[input() for _ in range(m)] for _ in range(n)]
[print(*r) for r in w]
print()
[print(*[w[j][i] for j in range(n)]) for i in range(m)]


j, i = [int(input()) for _ in range(2)]
c = [[input() for _ in range(i)] for _ in range(j)]
m = [[c[l][k] for l in range(j)]for k in range(i)]
[[print(*_) for _ in c], [print()], [print(*_) for _ in m]]


(lambda s: [[print(*c) for c in s], print(), [print(*c) for c in zip(*s)]])((lambda n, m: [[input() for _ in range(m)] for _ in range(n)])(int(input()), int(input())))
'''

#След матрицы



