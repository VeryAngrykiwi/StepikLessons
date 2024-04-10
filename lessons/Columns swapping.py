# Считываем размеры матрицы
n = int(input())
m = int(input())

# Создаем пустую матрицу
matrix = []

# Считываем элементы матрицы
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Считываем номера столбцов, которые нужно поменять местами
i, j = map(int, input().split())

# Меняем местами столбцы
for row in matrix:
    row[i], row[j] = row[j], row[i]

# Выводим измененную матрицу
for row in matrix:
    print(*row)

'''
n = int(input())  # количество строк
m = int(input())  # количество столбцов

# Ввод матрицы
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Ввод индексов столбцов для обмена
i, j = map(int, input().split())

# Меняем местами столбцы
while i < 0 or i >= m or j < 0 or j >= m:
    print("Некорректные индексы столбцов. Попробуйте снова.")
    i = int(input())
    j = int(input())

for row in matrix:
    row[i], row[j] = row[j], row[i]

# Вывод результата
for row in matrix:
    print(*row)


n, m = int(input()), int(input())
matrix = [input().split() for _ in range(n)]
col1, col2 = [int(i) for i in input().split()]

for i in range(n):
    matrix[i][col1], matrix[i][col2] = matrix[i][col2], matrix[i][col1]

for row in matrix:
    print(*row)


n, m = int(input()), int(input())
mult = [input().split() for _ in range(n)]
i, j = map(int, input().split())
for c in mult:
  c[i], c[j] = c[j], c[i]
  print(*c)



row, col = input().split()

matrix = [[int(x) for x in input().split()] for _ in range(int(row))]

inx1,  inx2 = input().split()
inx1, inx2 = int(inx1), int(inx2)

for m in matrix:
    m[inx1], m[inx2] = m[inx2], m[inx1]

for mx in matrix: print(*mx)


def print_matrix_rows(matrix: list, rows: int, cols: int, width=1):
  """
  :param matrix: матрица
  :param rows: количество строк
  :param cols: количество столбцов
  :param width:  требуемая длина строки
  :return: Перебор элементов матрицы по строкам
  """
  for r in range(rows):
      for c in range(cols):
          print(str(matrix[r][c]).ljust(width), end=' ')
      print()


n, m = int(input()), int(input())

# ввод матрицы
matrix = [[int(num) for num in input().split()] for _ in range(n)]

# ввод номеров столбцов для замены местами
col1, col2 = map(int, input().split())

# замена столцов местами
for i in range(n):
  matrix[i][col1], matrix[i][col2] = matrix[i][col2], matrix[i][col1]

# вывод матрицы на печать
print_matrix_rows(matrix, n, m)


n = int(input())
m = int(input())
mat = [[int(i) for i in input().split()] for j in range(n)]
ij = input()
i = int(ij[0])
j = int(ij[2])
for c in mat:
    c[i], c[j] = c[j], c[i]
    print(*c)


n, m = int(input()), int(input())
tab = [list(map(int, input().split())) for _ in range(n)]
i, j = map(int, input().split())
for c in range(n):
    tab[c][i], tab[c][j] = tab[c][j], tab[c][i]
    print(*tab[c])
'''

