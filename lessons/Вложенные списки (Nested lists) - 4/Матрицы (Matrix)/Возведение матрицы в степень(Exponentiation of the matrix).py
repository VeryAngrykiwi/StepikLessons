n = int(input())
mtx = [[int(i) for i in input().split()] for _ in range(n)]
mtx2 = mtx
m = int(input())

for _ in range(m-1):
    mtxTMP = [[0] * n for j in range(n)]
    for row in range(n):
        for rw in range(n):
            for col in range(n):
                mtxTMP[row][rw] += mtx[row][col]*mtx2[col][rw]
    mtx = mtxTMP

for row in mtxTMP:
    print(*row)


'''
def square_matrix_mult(matrixA, matrixB, size):
    matrixC = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for q in range(size):
                matrixC[i][j] += matrixA[i][q] * matrixB[q][j]
    return matrixC
    
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
m = int(input())
powered_matrix = matrix.copy()

for _ in range(m - 1):
    powered_matrix = square_matrix_mult(matrix, powered_matrix, n)

for row in powered_matrix:
    print(*row)
    
    
n = int(input())
m1 = [[int(j) for j in input().split()] for i in range(n)]
m = int(input())
res = m1

for l in range(m-1):
    res = [[sum([res[i][p] * m1[p][j] for p in range(n)]) for j in range(n)] for i in range(n)]

for r in res:
    print(*r)
    

def matrix_mult(m1, m2, n):
    return [[sum(m1[i][k] * m2[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

n = int(input())
a = [[*map(int, input().split())] for _ in range(n)]
# в качестве начального значения создаём единичную матрицу E
# у которой на главной диагонали все единицы. Она играет роль
# единицы при умножении матриц, т.е. E * A = A
res = [[0] * n for _ in range(n)]
for i in range(n):
    res[i][i] = 1
    
m = int(input())
while m:
    if m % 2 != 0:
        res = matrix_mult(res, a, n) # умножение на матрицу a
    a = matrix_mult(a, a, n) # возведение в квадрат   
    m //= 2
    
for row in res:
    print(*row)    
    


import numpy
a = int(input())
matrix = [[int(j) for j in input().split()]for i in range(a)]
for i in numpy.linalg.matrix_power(matrix, int(input())):
    print(*i)
    
    
    
n = int(input())
sip = [[int(i) for i in input().split()] for _ in range(n)]
m = int(input())

mat = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        for x in range(n):
            mat[i][j] += sip[i][x] * sip[x][j]
    
count = 0
zet = [[0] * n for _ in range(n)]
while count != m-1:
    zet = mat
    mat = [[0] * n for _ in range(n)]
    for r in range(n):
        for s in range(n):
            for t in range(n):
                mat[r][s] += sip[r][t] * zet[t][s]
    count += 1
    
for u in zet:
    print(*u)
print()


n = int(input())
matrix = [[*map(int, input().split())] for _ in range(n)]
matrix1 = matrix
for _ in range(int(input()) - 1):
    matrix1 = [[sum(matrix1[i][x] * matrix[x][j] for x in range(n)) for j in range(n)] for i in range(n)] 
[print(*matrix1[i]) for i in range(n)]



n = int(input())  # считали размерность 1-й матрицы n строк m столбцов
matr1 = [[0] * n for _ in range(n)]  # создаём матрицу 1
for i in range(n):  # заполняем строки 1-й матрицы
    matr1[i] = [int(a) for a in input().split()]  # заполняем ячейки 1 матрицы

m = int(input())  # считали размерность степень
matr2 = [[0] * n for _ in range(n)]  # создаём матрицу 2
for i in range(n):
    for j in range(n):
        matr2[i][j] = matr1[i][j]  # заполняем строки матрицы списками чисел

matr3 = [[0] * n for _ in range(n)]  # создаём матрицу 3
for a in range(m - 1):
    for i in range(n):
        for j in range(n):
            for l in range(n):
                matr3[i][j] += matr1[i][l] * matr2[l][j]
        matr1[i] = matr3[i]
        matr3[i] = [0] * n


for r in range(n):  # выводим матрицу с расширением
    for c in range(n):
        print(matr1[r][c], end=' ')  
    print()
'''