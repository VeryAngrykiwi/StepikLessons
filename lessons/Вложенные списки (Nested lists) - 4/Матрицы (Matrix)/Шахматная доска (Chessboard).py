def fill_matrix(n, m):
  mtx = []
  i = 0
  while i < n:
      row = []
      j = 0
      while j < m:
          if (j % 2 == 1 and i % 2 == 0) or (j % 2 == 0 and i % 2 == 1):
              row.append('*')
          else:
              row.append('.')
          j += 1
      mtx.append(row)
      i += 1
  return mtx

n,m = map(int, input().split())
mtx = fill_matrix(n, m)
[print(*row) for row in mtx]


'''
n, m = [int(i) for i in input().split()]
board = [['.'] * m for _ in range(n)]

for i in range(n):
    for j in range(1 - i % 2, m, 2):
        board[i][j] = '*'

for row in board:
    print(*row)



n, m = map(int, input().split())
for i in range(n):
    row = ['.' if (i + j) % 2 == 0 else '*' for j in range(m)]
    print(*row)



n, m = map(int, input().split())
b = [['.*'[(i + j) % 2] for j in range(m)] for i in range(n)]
for row in b:
    print(*row)


pos = [int(i) for i in input().split()]
for i in range(pos[0]):
    for j in range(pos[1]):
        if i % 2 == j % 2:
            print('.', end = ' ')
        else:
            print('*', end = ' ')
    print()



n, m = map(int, input().split())
[print(*[['.', '*'][(i + j)% 2] for j in range(m)]) for i in range(n)]



a, b = map(int,input().split())
[print(*['.'  if (j + i) % 2 == 0 else '*' for j in range(b)]) for i in range(a)]



n, m = input().split()
n, m = int(n), int(m)
matrix = [['.' for _ in range(m) ] for _ in range(n)]

for i in range(n):    
    for j in range(m):
        if (i + j + 1) % 2 == 0:
            matrix[i][j] = '*'
for i in range(n):
    print(*matrix[i])



st = input()
n = int(st.split()[0])
m = int(st.split()[1])
matrix = []
z = []
for i in range(n):
    for j in range(m):
        if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
            z.append('.')
        elif (i % 2 != 0 and j % 2 == 0) or (i % 2 == 0 and j % 2 != 0):
            z.append('*')
    matrix.append(z)
    z = []
for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(2), end='')
    print()
'''