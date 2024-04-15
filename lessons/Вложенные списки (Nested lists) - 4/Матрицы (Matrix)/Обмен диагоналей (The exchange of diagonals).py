n = int(input())
mtx = [input().split() for _ in range(n)]

for i in range(n):
  mtx[i][i], mtx[n - i - 1][i] = mtx[n - i - 1][i], mtx[i][i]

[print(*row) for row in mtx]

'''
n = int(input())
mtx = []

mtxapp = 0
while mtxapp < n:
  tmp = list(map(int, intput().split()))
  mtxapp += 1

i = 0
while i < n:
  mtx[i][i], mtx[n - i - 1][i] = mtx[n - i - 1][i], mtx[i][i]
  i += 1

p = 0
while p < len(mtx):
  print(*mtx[p])
  p += 1


a = [list(map(int, input().split())) for _ in range(int(input()))]
for i in range(len(a)):
    a[i][i], a[-i - 1][i] = a[-i - 1][i], a[i][i] 
[print(*a[i]) for i in range(len(a))]



x = int(input())
mtx = [[int(n) for n in input().split()] for _ in range(x)]

for i in range(x):
    for j in range(1, x + 1):
        if i == j - 1:
            mtx[i][i], mtx[-j][i] = mtx[-j][i], mtx[i][i]

[print(*m) for m in mtx]



def print_matrix_rows(matrix: list, rows: int, cols: int, width=1) -> None:
    """
    :param matrix: матрица
    :param rows: количество строк
    :param cols: количество столбцов
    :param width:  требуемая длина строки
    :return: печатает элементы матрицы по строкам
    """
    for r in range(rows):
        for c in range(cols):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


n = int(input())



def read_matrix():
  rows = int(input())
  return [[int(x) for x in input().split()] for i in range(rows)]

def print_matrix(a):
  for row in a:
      print(*row)

def swap_diag(a):
  n = len(a)
  for i in range(n):
      a[i][i], a[n-1-i][i] = a[n-1-i][i], a[i][i]

a = read_matrix()
swap_diag(a)
print_matrix(a)
'''