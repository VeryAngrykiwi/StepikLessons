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
