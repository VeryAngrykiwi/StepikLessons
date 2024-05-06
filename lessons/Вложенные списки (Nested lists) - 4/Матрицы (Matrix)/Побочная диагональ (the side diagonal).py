n = int(input())
mtx = []
for _ in range(n):
  tmp = [int(e) for e in range(n)]
  mtx.append(tmp)

for i in range(n):
  for q in range(n):
    if i == n - 1 - q:
      mtx[i][q] = 1
    elif i < n - 1 - q:
      mtx[i][q] = 0
    elif i > n - 1 - q:
      mtx[i][q] = 2

for i in range(n):
  print(*mtx[i])


'''
n = int(input())
matrix = [[None for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i + j + 1 == n:
            matrix[i][j] = 1
        elif i + j + 1 < n:
            matrix[i][j] = 0
        else:
            matrix[i][j] = 2

for row in matrix:
    print(*row)



def f(i, j, n):
  if i == n - j - 1:
      return 1
  elif i < n - j - 1:
      return 0
  else:
      return 2

n = int(input())

res = [[f(i, j, n) for j in range(n)] for i in range(n)]

for x in res:
  print(*x)



n = int(input())
q = [[(i >= n - j - 1) + (i > n - j - 1) for j in range(n)] for i in range(n)]
for e in q:
    print(*e)



n = int(input())
board = [[0] * (n - i - 1) + [1] + [2] * i for i in range(n)]

for row in board:
    print(*row)

    

n = int(input())

for i in range(n):
    print('0 ' * (n - i - 1) + '1' + ' 2' * i)



n = int(input())

[print(*[0 if i + j + 1 < n else 2 if i + j + 1 > n else 1 for j in range(n)]) for i in range(n)]



n = int(input())
[print(*[(i > (n - j - 1)) + int(i >= (n - j - 1)) for j in range(n)]) for i in range(n)]
'''