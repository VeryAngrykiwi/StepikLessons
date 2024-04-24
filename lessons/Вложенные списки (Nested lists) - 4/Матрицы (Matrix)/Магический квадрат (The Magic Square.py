n = int(input())
mtx = [input().split() for _ in range(n)]

rowSum = 0
columnSum = 0
diagMainSum = 0
diagSideSum = 0

for row in mtx:
    rowSum = sum(int(num) for num in row)

for i in range(n):
  columnSum = 0
  for j in range(n):
    columnSum += int(mtx[j][i])

diagMainSum = sum(int(mtx[i][i]) for i in range(len(mtx)))

diagSideSum = sum(int(mtx[n-j-1][j]) for j in range(n))

seq_true = ''
if len({mtx[i][j] for i in range(n) for j in range(n)}) !=n**2 or any('0' in row for row in mtx):
    seq_true = False
else:
    seq_true = True

square_find = False
if (any(str(n**2) in row for row in mtx)):
    square_find = True

if rowSum == columnSum == diagMainSum == diagSideSum and seq_true == square_find == True:
  print('YES')
else:
  print('NO')

'''
def is_magic_square(n, matrix):
  # создаем список для всех чисел правильной матрицы
  correct_nums = list(range(1, n ** 2 + 1))

  # создаем список для всех чисел нашей матрицы
  our_nums = []
  for row in matrix:
      our_nums.extend(row)

  # если эти списки не равны, значит наша матрица уже не состоит из всех чисел от 1 до n ** 2
  # значит, мы сразу можем вернуть "NO" и не продолжать дальнейшие проверки
  our_nums.sort()
  if our_nums != correct_nums:
      return "NO"

  # в самой матрице мы уже храним все ряды (строки)
  rows = matrix.copy()

  # создаем список для всех столбцов
  columns = []
  for j in range(n):
      cur_column = []
      for i in range(n):
          cur_column.append(matrix[i][j])

      columns.append(cur_column)

  # создаем список для диагоналей (с двумя пустыми подсписками)
  diagonals = [[], []]
  for i in range(n):
      diagonals[0].append(matrix[i][i])
      diagonals[1].append(matrix[i][n - 1 - i])

  # соединям все строки, столбцы и диагонали в один список
  all_lines = rows + columns + diagonals

  # инициализируем переменные для максимальной и минимальной суммы среди всех "линий"
  # за начальные значения возьмём сумму первой "линии"
  max_sum = sum(all_lines[0])
  min_sum = sum(all_lines[0])
  for line in all_lines:
      max_sum = max(max_sum, sum(line))
      min_sum = min(min_sum, sum(line))

  # теперь просто сравниваем максимальную и минимальную суммы
  # они должны быть равны, т.к. все суммы должны быть равны
  if max_sum != min_sum:
      return "NO"

  return "YES"

n = int(input())
matrix = [[int(el) for el in input().split()] for _ in range(n)]

print(is_magic_square(n, matrix))



def magic_square():

    cols = int(input())
    matrix = []
    sum_main_diag = 0
    sum_semi_diag = 0
    check = []

    for i in range(cols):                                # заполняем матрицу
        elem = [int(num) for num in input().split()]
        matrix.append(elem)

    for i in range(cols):                                # заполняем проверочный список всеми элементами матрицы
        check += matrix[i]

    for i in range(1, len(check) + 1):                   # проверяем проверочный список на наличие всех чисел в промежутке от 1 до n ** 2
        if i not in check:
            return print("NO")                           # если нет какого-то числа, то значит дальше нет смысла проверять равенство, завершаем с NO

    for i in range(cols):                                # проверяем равенство диагоналей
        sum_main_diag += matrix[i][i]
        sum_semi_diag += matrix[i][cols - 1 - i]

    for i in range(cols):                                # проверяем равенство строк, столбцов и диагоналей
        sum_cols = 0
        sum_rows = 0
        for j in range(cols):
            sum_cols += matrix[i][j]
            sum_rows += matrix[j][i]
        if not sum_cols == sum_rows == sum_main_diag == sum_semi_diag:
            return print("NO")                           # если что-то не равно, завершаем с NO
    else:
        return print("YES")                              # если всё хорошо, завершаем с YES


magic_square()



def sum_matrix(n, total, matrix):
    total += sum(matrix[i][j] for j in range(n) for i in range(n)) # сумма строк
    total += sum(matrix[j][i] for j in range(n) for i in range(n)) # сумма столбцов
    total += sum(matrix[i][i] for i in range(n)) # сумма главной диагонали
    total += sum(matrix[i][n-i-1] for i in range(n)) # сумма второстепенной диагонали
    return total

n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
total = 0
total = sum_matrix(n, total, matrix) / (n + n + 2) # сумма матрицы деленная на количество столбцов, строк и диаг
flag = False
l = [matrix[i][j] for j in range(n) for i in range(n)]
l.sort()
if l == [i for i in range(1, n ** 2 + 1)]:
    flag = True
print('YES' if total == sum(matrix[-1]) and flag == True else 'NO')



n = int(input()); m = []; b=[]
for i in range(n):
    a = [int(j) for j in input().split()]
    m.append(a)
    b += a
t = 'YES'    
if sorted(b) != list(range(1, n**2 + 1)): t = 'NO' 
mm = [[m[i][j] for i in range(n)] for j in range(n)]
s = sum(m[0])
for i in range(n):
    if sum(m[i]) != s or sum(mm[i]) != s:
        t = 'NO'
        break
print(t)



n = int(input())
a = [[*map(int, input().split())] for _ in range(n)]
k = n * (1 + n ** 2) // 2                                                      # магическая константа
print(('NO', 'YES')[all(sum(e) == k for x in (((a[i][i] for i in range(n)),    # глав. диагональ
                                               (a[i][~i] for i in range(n))),  # втор. диагональ
                                               a,                              # строки
                                               zip(*a))                        # столбцы
                                               for e in x)           
                                               and
                    set(sum(a, [])) == set(range(1, n ** 2 + 1))               # натур. ряд до n^2.          
                   ])



n = int(input())
a = [[*map(int, input().split())] for _ in range(n)]
k = n * (1 + n ** 2) // 2  # магическая константа
print('YES' if all(sum(x) == k for x in (*a, *zip(*a), [a[i][i] for i in range(n)], [a[i][~i] for i in range(n)])) else 'NO')



import numpy as np
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
v = {*np.sum(a, axis=1), *np.sum(a, axis=0), sum(np.diag(a)), sum(np.fliplr(a).diagonal())}
if len(v) == 1:
    print('YES')
else:
    print('NO')



import numpy as np
n = int(input())
data = np.array([input().split() for _ in range(n)]).astype(int)
uniq_sums = set([*np.sum(data, axis = 0), *np.sum(data, axis = 1),
                     sum(np.diag(data)), sum(np.diag(np.fliplr(data)))])
print("YES" if len(uniq_sums) == 1 and \
      np.all(np.sort(data.flatten()) == np.arange(n * n) + 1)
      else "NO")


n = int(input()) # ввод
matrix = [] # пустая матрица
for _ in range(n): # наполнение матрицы
#  matrix.append(list(map(int, input().split())))
  tmp = [int(x) for x in input().split()]
  matrix.append(tmp)
# digits = list(range(1, n ** 2 + 1)) # список чисел от 1 до n ** 2)
digits = [i for i in range(1, n**2 + 1)] # список чисел от 1 до n^2 проверочная матрица (изначальный список)

d1, d2 = 0, 0 # начальные суммы диагоналей
for i in range(n): # вычисления
  stolb_sum, stroka_sum = 0, 0 # начальные суммы столбца и строки
  for j in range(n):
    stolb_sum += matrix[j][i] # суммы столбцов
    stroka_sum += matrix[i][j] # суммы строк
    if matrix[i][j] in digits: # удаление из списка чисел (проверочная матрица) элемнтов матрицы
      digits.remove(matrix[i][j])
  d1 += matrix[i][i] # сумма главной диагонали
  d2 += matrix[i][n-i-1] #сумма побочной диагонали
  if stolb_sum != stroka_sum: # проверка суммы столбцов и строк
    break

if stolb_sum == stroka_sum == d1 == d2 and digits == []: # проверка равенства значений (магическое совпадение 🤣)
  print('YES')
else:
  print('NO')
'''