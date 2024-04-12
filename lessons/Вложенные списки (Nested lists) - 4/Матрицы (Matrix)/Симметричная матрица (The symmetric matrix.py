n = int(input())
mtx = []
flag = True
mtx = [input().split() for _ in range(n)]
'''''
for _ in range(n):
  tmp = list(map(int, input().split()))
  mtx.append(tmp)
'''

for i in range(n):
  for j in range(n):
    if mtx[i][j] != mtx[j][i] and i != j:
      flag = False
      break

if flag:
  print("YES")
else:
  print("NO")

[print(*row) for row in mtx]

'''
n = int(input())
matrix = [input().split() for _ in range(n)]
result = 'YES'

for i in range(n):
    for j in range(i + 1, n):
        if matrix[i][j] != matrix[j][i]:
            result = 'NO'
            break
    if result == 'NO':
        break

print(result)



n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
if all([matrix[i][j] == matrix[j][i] for j in range(n) for i in range(n)]):
    print('YES')
else:
    print('NO')



n = int(input())

matrix = [[int(item) for item in input().split()] for _ in range(n)]
matrix_T = [[matrix[i][j] for i in range(n)] for j in range(n)]

if (matrix == matrix_T):
    print("YES")
else:
    print("NO")



n = int(input())
matrix = [[int(j) for j in input().split()] for _ in range(n)]
print('YES' if all([matrix[i][j] == matrix[j][i] for j in range(n) for i in range(n)]) else 'NO')



m = [tuple(map(int, input().split())) for _ in range(int(input()))]
print(('NO', 'YES')[m == [*zip(*m)]])



n = int(input())
is_symmetric = True
t = [input().split() for _ in range(n)]
for i in range(n):
    for j in range(i):
        if t[i][j] != t[j][i]:
            is_symmetric = False
            break
    if not is_symmetric:
        break
print('YES' if is_symmetric else 'NO')



x = [[int(i) for i in input().split()] for _ in range(int(input()))]

def foo():
    for i in range(len(x)):
        for j in range(len(x)):
          if x[j][i] != x[i][j]:
            return "NO"
    return "YES"

print(foo())

'''
