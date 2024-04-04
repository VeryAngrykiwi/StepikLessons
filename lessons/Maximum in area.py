n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

max_element = matrix[n-1][0]
for i in range(n):
    for j in range(n):
        if i >= j:
            max_element = max(max_element, matrix[i][j])

print(max_element)

'''
n = int(input())
matrix = []
for k in range(n):
    tmp = [int(x) for x in input().split()]
    matrix.append(tmp)

max = matrix[0][0]

for i in range(n):
    for q in range(n):
        if i >= q and matrix[i][q] > max:
            max = matrix[i][q]

print(max)


print(max(e for i in range(int(input())) for e in input().split()[:i + 1]))


n = int(input())
l = []
for i in range(n):
    l.extend([int(x) for x in input().split()][0:i+1])

print(max(l))


n=int(input())
matrix=[[int(i) for i in input().split()] for _ in range(n)]
print(max(max(matrix[i][j] for j in range(i+1)) for i in range(n)))



n = int(input())
maximum = -1000000000000000000000000000000000000000000000000000000000000
for i in range(n):
    a = [int(k) for k in input().split()]
    maximum = max(max(a[:i+1]), maximum)

print(maximum)


n = int(input())  # ввод размера матрицы
matrix = []  # пустой список для матрицы
for i in range(n):
    temp = [int(num) for num in input().split()]  # создание матрицы списочным выражениям
    matrix.append(temp)  # добавление в пустой список

result = []  # создаем пуйстой список   
for x in range(n):
    for j in range(n):  # проходимся по матрицы
        if x == j:  # если x = j, то добавляем в список result
            result.append(matrix[x][j])
        elif x > j:  # если x > j, то добавяем в список result
            result.append(matrix[x][j])
print(max(result))  # выводим на экран
'''