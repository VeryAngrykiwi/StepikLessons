n = int(input())
mtx = [input().split() for _ in range(n)]

for i in range(n):
  for j in range(-1, -n-1,-1):
    print(mtx[j][i], end = ' ')
  print()

'''
n = int(input())
matrix = [input().split() for _ in range(n)]
result = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        result[i][j] = matrix[n - j - 1][i]

for row in result:
    print(*row)



n = int(input())
matrix = [input().split() for _ in range(n)]
res_matrix = []

for j in range(n):
    cur_column = []  # список для текущего столбца
    for i in range(n):
        cur_column.append(matrix[i][j])

    # полученный столбец мы переворачиваем и запихиваем как ряд в результирующий список
    res_matrix.append(cur_column[::-1])

for row in res_matrix:
    print(*row)



matrix = []

for _ in range(int(input())):
    matrix.append([int(x) for x in input().split()])

for row in zip(*matrix[::-1]):
    print(*row)


n = int(input())
a = [input().split() for _ in range(n)]
[print(*[a[n-j-1][i] for j in range(n)]) for i in range(n)]



n = int(input())

array = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n)[::-1]:
        print(array[j][i], end=' ')
    print()



def read_square_matrix():
    size = int(input())
    return [list(map(int, input().strip().split())) for _ in range(size)]

def rotate_matrix_clockwise(m):
    m.reverse()
    for r in range(1, len(m)):
        for c in range(r):
            m[r][c], m[c][r] = m[c][r], m[r][c]

def print_matrix(matrix):
    for row in matrix:
        print(*row)

def main():
    matrix = read_square_matrix()
    rotate_matrix_clockwise(matrix)
    print_matrix(matrix)

main()



def turn_right_90(matrix, n):
  return [[matrix[i][j] for i in range(n - 1, -1, -1)] for j in range(n)]

def print_square_matrix(matrix, n, width):
  for i in range(n):
      for j in range(n):
          print(str(matrix[i][j]).ljust(width), end=' ')
      print()

size = int(input())
my_matrix = [list(map(int, input().split())) for _ in range(size)]
print_square_matrix(turn_right_90(my_matrix, size), size, 0)



[print(*row[::-1]) for row in zip(*[list(map(int,input().split())) for _ in range(int(input()))])]



import numpy as np
n = int(input())
a = np.array([input().split() for _ in range(n)], dtype=int)
for x in a.T[:, ::-1]:
    print(*x)
'''

