# вводные данные матрицы
n, m = map(int, input().split()) 
mtx1 = [list(map(int, input().split())) for _ in range(n)]
input() # пустая строка()
m, k = map(int, input().split())
mtx2 = [list(map(int, input().split())) for _ in range(m)]

# перемножение матрицы list comprehension
result = [
    [
        sum(mtx1[i][p] * mtx2[p][j] for p in range(m)) 
        for j in range(k)
    ] 
    for i in range(n)
]

#вывод матрицы
for row in result:
    print(*row)


'''
n, m = [int(i) for i in input().split()]
matrixA = [[int(i) for i in input().split()] for _ in range(n)]
input()
m, k = [int(i) for i in input().split()]
matrixB = [[int(i) for i in input().split()] for _ in range(m)]
matrixC = [[0] * k for _ in range(n)]

for i in range(n):
    for j in range(k):
        for q in range(m):
            matrixC[i][j] += matrixA[i][q] * matrixB[q][j]

for row in matrixC:
    print(*row)



n1, m1 = map(int, input().split())
matrix1 = [list(map(int, input().split()))for i in range(n1)]
input()
n2, m2 = map(int, input().split())
matrix2 = [list(map(int, input().split()))for i in range(n2)]
matrix3 = [[sum([matrix1[i][k] * matrix2[k][j] for k in range(m1)])for j in range(m2)]for i in range(n1)]
for i in matrix3:
    print(*i)



n, m = map(int, input().split())
a = [[int(i) for i in input().split()] for _ in range(n + 1)]
t = int(input().split()[1])
b = [[int(i) for i in input().split()] for _ in range(m)]
[print(*[sum(a[i][j] * b[j][k] for j in range(m)) for k in range(t)]) for i in range(n)]  
'''