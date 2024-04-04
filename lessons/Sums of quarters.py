n = int(input())
matrix = []
for k in range(n):
    tmp = [int(x) for x in input().split()]
    matrix.append(tmp)

sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0

for i in range(n):
    for j in range(n):
      if i < j and i < n - 1 - j:
        sum1 += matrix[i][j]  
      elif i < j and i > n - 1 - j:
        sum2 += matrix[i][j]
      elif i > j and i > n - 1 - j:
        sum3 += matrix[i][j]  
      elif i > j and i < n - 1 - j:
        sum4 += matrix[i][j]

print(f'Верхняя четверть: {sum1}\nПравая четверть: {sum2}\nНижняя четверть: {sum3}\nЛевая четверть: {sum4}')

'''
n = int(input())
matrix = []
quadrants = [['Верхняя четверть:', 0], 
             ['Правая четверть:', 0],
             ['Нижняя четверть:', 0], 
             ['Левая четверть:', 0]]

for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)

for i in range(n):
    for j in range(n):
        if i < j and i + j + 1 < n :
            quadrants[0][1] += matrix[i][j]
        elif i < j and i + j + 1 > n:
            quadrants[1][1] += matrix[i][j]
        elif i > j and i + j + 1 > n:
            quadrants[2][1] += matrix[i][j]
        elif i > j and i + j + 1 < n:
            quadrants[3][1] += matrix[i][j]

for i in range(4):
    print(quadrants[i][0], quadrants[i][1])



n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
upper, lower, left, right = 0, 0, 0, 0

for i in range(n):
    upper += sum(matrix[i][i+1:n-i-1])
    left += sum(matrix[i][:min(i, n-i-1)])
    right += sum(matrix[i][max(n-i, i+1):])
    lower += sum(matrix[i][n-i:i])

print(f'Верхняя четверть: {upper}')
print(f'Правая четверть: {right}')
print(f'Нижняя четверть: {lower}')
print(f'Левая четверть: {left}')


n = int(input())
m = [[int(i) for i in input().split()] for _ in range(n)]
sm = [0] * 4
quarters = ('Верхняя', 'Правая', 'Нижняя', 'Левая')
for i in range(n // 2):
    for j in range(i+1, n-i-1):
        for k, e in enumerate((m[i][j], m[j][~i], m[~i][j], m[j][i])):
            sm[k] += e

print(*(f'{q} четверть: {sm[i]}' for i, q in enumerate(quarters)), sep='\n') 


n = int(input())
mtr = [[int(ch) for ch in input().split()] for _ in range(n)]
print('Верхняя четверть:', sum([mtr[i][j] for i in range(n) for j in range(n) if (i < j and i < n - 1 - j)]))
print('Правая четверть:', sum([mtr[i][j] for i in range(n) for j in range(n) if (i < j and i > n - 1 - j)]))
print('Нижняя четверть:', sum([mtr[i][j] for i in range(n) for j in range(n) if (i > j and i > n - 1 - j)]))
print('Левая четверть:', sum([mtr[i][j] for i in range(n) for j in range(n) if (i > j and i < n - 1 - j)]))


n = int(input())
mtx = [list(map(int, input().split())) for i in range(n)]
out = [['Верхняя четверть:', 0], ['Правая четверть:', 0], ['Нижняя четверть:', 0], ['Левая четверть:', 0]]
for i in range(n):
    for j in range(n):
        if i < j and i < n - 1 - j:
            out[0][1] += mtx[i][j]
        elif j > i > n - 1 - j:
            out[1][1] += mtx[i][j]
        elif i > j and i > n - 1 - j:
            out[2][1] += mtx[i][j]
        elif j < i < n - 1 - j:
            out[3][1] += mtx[i][j]
[print(i, j) for i, j in out]


n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
print('Верхняя четверть:', sum(matrix[i][j] for i in range(n) for j in range(n) if i < j and i < n-1-j))
print('Правая четверть:', sum(matrix[i][j] for i in range(n) for j in range(n) if j > i > n-1-j))
print('Нижняя четверть:', sum(matrix[i][j] for i in range(n) for j in range(n) if i > j and i > n-1-j))
print('Левая четверть:', sum(matrix[i][j] for i in range(n) for j in range(n) if n-1-j > i > j))


quarters = [['Верхняя четверть', 0], ['Правая четверть', 0], ['Левая четверть', 0], ['Нижняя четверть', 0]]
n = int(input())
for i in range(n):
    for j, elem in enumerate(input().split()):
        if i != j and i != n - 1 - j:
            ind = (i > j) * 2 + (i > (n - 1 - j))
            quarters[ind][1] += int(elem)
for i in [0, 1, 3, 2]:
    print(f'{quarters[i][0]}: {quarters[i][1]}')
'''