n, m = map(int, input().split())
a = [[int(i) for i in input().split()] for _ in range(n)]
input()
b = [[int(i) for i in input().split()] for _ in range(n)]

for i in range(n):
    for j in range(m):
        print(a[i][j] + b[i][j], end=' ')
    print()




'''
n, m = [int(i) for i in input().split()]
matrixA = [[int(i) for i in input().split()] for _ in range(n)]
input()
matrixB = [[int(i) for i in input().split()] for _ in range(n)]
matrixC = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrixC[i][j] = matrixA[i][j] + matrixB[i][j]

for row in matrixC:
    print(*row)



n, m = [int(x) for x in input().split()]

A = [[int(x) for x in input().split()] for _ in range(n)]
input()
B = [[int(x) for x in input().split()] for _ in range(n)]

C = [[A[i][j] + B[i][j] for j in range(m)] for i in range(n)]

for x in C:
    print(*x)

 

n, m = map(int, input().split())
arra = [list(map(int, input().split())) for _ in range(n)]
input()
arrb = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    print(*list(x + y for x, y in zip(arra[i], arrb[i])))



def summatr(matr1, matr2, n, m):
  newmatr = [[0 for _ in range(m)] for _ in range(n)]
  for i in range(n):
    for j in range (m):
      newmatr[i][j] = matr1[i][j] + matr2[i][j]
  return newmatr

n, m = list(map(int, input().split()))
matr = [[int(i) for i in input().split()] for j in range(n*2+1)]
matr1, matr2 = matr[:n], matr[n+1:]

for i in summatr(matr1, matr2, n, m):
  print(*i)



# Принимаем размеры матриц
n, m = map(int, input().split())

# Принимаем сами матрицы
a = [[*map(int, input().split())] for _ in range(n)]
s = input()
b = [[*map(int, input().split())] for _ in range(n)]

# Суммируем
res = new_matrix = [[(a[i][j] + b[i][j]) for j in range(m)] for i in range(n)]

# Печатаем результат
[print(*res[i]) for i in range(n)]

'''