n, m = int(input()), int(input())
matrix = []

for k in range(n):
    matrix.append(list(map(int, input().split())))
#   tmp = [int(x) for x in input().split()]
#   matrix.append(tmp)
x = 0
y = 0
matrix_max = matrix[0][0]

for i in range(n):
  for q in range(m):
    if matrix[i][q] > matrix_max:
      matrix_max = matrix[i][q]
      x = i
      y = q

print(x, y)

'''
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
w = [list(map(int, input().split())) for i in range(n)]
ww = [max(i) for i in w]
r = ww.index(max(ww))
c = w[r].index(max(ww))
print(r, c)



n, m = int(input()), int(input())
matrix = [int(num) for _ in range(n) for num in input().split()]
print(matrix.index(max(matrix)) // m, matrix.index(max(matrix)) % m)



n, m, arr = int(input()) , int(input()), []
for _ in range(n):
    arr += list(map(int, input().split()))
print(arr.index(max(arr)) // m, arr.index(max(arr)) % m)
'''