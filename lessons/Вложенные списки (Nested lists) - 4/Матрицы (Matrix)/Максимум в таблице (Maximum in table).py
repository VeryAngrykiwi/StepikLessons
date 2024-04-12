n, m = int(input()), int(input())
mtx = []

for k in range(n):
    mtx.append(list(map(int, input().split())))
x = 0
y = 0
mtx_max = mtx[0][0]

for i in range(n):
    for q in range(m):
        if mtx[i][q] > mtx_max:
            mtx_max = mtx[i][q]
            x = i
            y = q

print(x, y)



'''
n, m = int(input()), int(input())
largest = -10 ** 6
mult = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
  for j in range(m):
    while largest < mult[i][j]:
      largest = mult[i][j]
      x, y = i, j
print(x, y)



n, m = int(input()), int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
row, col = 0, 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] > matrix[row][col]:
            row,col = i, j

print(row, col)



n, m = int(input()), int(input())
maxi, maxj = 0, 0
dat = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if dat[i][j] > dat[maxi][maxj]:
            maxi, maxj = i, j
print(maxi, maxj)



_, m, *lst = map(int, open(0).read().split())
print(*divmod(max(enumerate(lst), key=lambda x: x[1])[0], m))



n, m = [int(input()) for __ in range(2)]
matrix = [list(map(int, input().split())) for i in range(n)]
max_x = max([max(i) for i in matrix])
for i in range(len(matrix)):
  if max_x in matrix[i]:
    print(i, matrix[i].index(max_x))
    break


n, m = int(input()), int(input())
matrix = [int(num) for _ in range(n) for num in input().split()]
print(matrix.index(max(matrix)) // m, matrix.index(max(matrix)) % m)



n, m = int(input()), int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
max = -10
for i in range(n):
    for j in range(m):
        if matrix[i][j] > max:
            max = matrix[i][j]
flag = True
for i in range(n):
    if flag:
        for j in range(m):
            if matrix[i][j] == max:
                print(i, j)
                flag = False
                break



n = int(input())
m = int(input())
x = [list(map(int, input().split())) for _ in range(n)]
mx = [0, 0]
for i in range(n):
    for j in range(m):
        if x[i][j] > x[mx[0]][mx[1]]:
            mx = [i, j]
print(*mx)



n, m = [int(input()) for _ in 'nm']

mtrx = [int(i) for j in range(n) for i in input().split()]

print(*divmod(mtrx.index(max(mtrx)), m))



n, m = int(input()), int(input())
matrix = []
for i in range(n):
    matrix.append([int(j) for j in input().split()])
highest = max(max(matrix, key=max))
i, j = 0, 0
while matrix[i][j] != highest:
    if j == m - 1:
        i += 1
        j = 0
    else:
        j += 1
print(i, j)
'''