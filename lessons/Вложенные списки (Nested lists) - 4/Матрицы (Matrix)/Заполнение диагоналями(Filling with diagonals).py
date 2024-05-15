# Вариант 1:
n, m = map(int, input().split())
mtx = [[0 for _ in range(m)] for _ in range(n)]

num = 1
for j in range(m+n-1):
    for i in range(n):
        if j - i in range(m):
            mtx[i][j - i] = num
            num += 1

for i in range (n):
    for j in range(m):
        print(str(mtx[i][j]).ljust(2), end= ' ')
    print()

# Вариант 2:
# вход строка чисел
x = input().split()

# считывание строки чисел
n, m = int(x[0]), int(x[1])

# создание пустой матрицы
mtx = []

# построение матрицы методом append, наполнение условным объектом e.
for _ in range(n):
    tmp = [e for e in range(m)]  # временная переменная наполняющая матрицу (list comprehension,генератор списков)
    mtx.append(tmp)  # наполнение матрицы

# наполнение матрицы числами в соответствии с условием
num = 1 # счетчик
for k in range(n * m):  # размер матрицы, цикл по всей матрице
    for i in range(n):  # цикл по строкам
        for j in range(m):  # цикл по столбцам
            if i + j == k:  # условие сумма индексов (столбец) по диагонали.
                mtx[i][j] = num
                num += 1

# печать матрицы с отступами, методом str.
for i in range(n):
    for j in range(m):
        print(str(mtx[i][j]).ljust(2), end=' ')
    print()

'''
n, m = [int(el) for el in input().split()]
matrix = [[None for _ in range(m)] for _ in range(n)]
cnt = 1

# проходим по всем диагоналям
for d in range(n + m - 1):
    for i in range(n):
        for j in range(m):
            if i + j == d:
                matrix[i][j] = cnt
                cnt += 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end="")
    print()
    


n, m = [int(i) for i in input().split()]

matrix = [[1] * m for _ in range(n)]
row, col, diag = 0, 0, 0

for i in range(1, n * m):
    col -= 1
    row += 1
    if col < 0 or row == n:
        diag += 1
        col = diag if diag < m else m - 1
        row = diag - col
    
    matrix[row][col] += i

[print(*i) for i in matrix]



n, m = map(int, input().split())
mt = [[''] * m for i in '1'* n]
d = 1
for k in range(1, n + m + 1):
    for i in range(n):
        for j in range(m):
            if i + j + 1 == k:
                mt[i][j] = str(d).ljust(3)
                d += 1
[print(*r, sep='') for r in mt]



# Принимаем параметры матрицы
n, m = map(int, input().split())
# Создаем скелет матрицы
matrix = [[0] * m for i in range(n)]
# Задаем отсчет с единицы
d = 1

for k in range(1, n + m):               # Цикл перебирающий сумму индексов в диагонали
    for i in range(n):                  # Перебираем строки
        for j in range(m):              # Перебираем столбцы
            if i + j + 1 == k:          # Выявляем ячейки, относящиеся к искомой диагонали
                matrix[i][j] = d        # Присваиваем обнаруженной ячейке порядковый номер
                d += 1                  # Обновляем счетчик

# Распечатываем полученную матрицу
for row in range(n):
    for col in range(m):
        print(str(matrix[row][col]).ljust(3), end=' ')
    print()



(n, m), cnt = map(int, input().split()), 1
a = [[0] * m for _ in range(n)]
for d in range(m + n - 1):
    for i in range(max(0, d - m + 1), min(d, n - 1) + 1):
        a[i][d - i], cnt = cnt, cnt + 1
for row in a:
    print(*map(lambda x: f'{x:<2}', row))
    
   

[n, m] = [int(i) for i in input().split()]
matrix = [['0']*m for _ in range(n)] 
num = 0

for d in range(m + n - 1):
    for i in range(n):
        j = d - i
        if 0 <= i < n and 0 <= j < m:
            num += 1
            matrix[i][j] = str(num).ljust(3)
            

for i in range(n):
    print(*matrix[i])
    

list = input().split()
a = int(list[0])
b = int(list[1])
matrix = []
elem = []
total = 0

if a > b:
    for i in range(a):
        for k in range(b):
            diagonals = i + k + 1
            old_diagonals = diagonals - 1
            for h in range(1, old_diagonals + 1):
                if h < b:
                    total += h
                elif b <= h <= a:
                    total += b
                elif h > a:
                    total += b - (h - a)
            if diagonals <= b:
                total += i + 1
            elif diagonals > b:
                total += (i + 1) - (diagonals - b)
            elem.append(total)
            total = 0
        matrix.append(elem)
        elem = []
elif b > a:
    for i in range(a):
        for k in range(b):
            diagonals = i + k + 1
            old_diagonals = diagonals - 1
            for h in range(1, old_diagonals + 1):
                if h < a:
                    total += h
                elif a <= h <= b:
                    total += a
                elif h > b:
                    total += a - (h - b)
            if diagonals <= b:
                total += i + 1
            elif diagonals > b:
                total += (i + 1) - (diagonals - b)
            elem.append(total)
            total = 0
        matrix.append(elem)
        elem = []
elif a == b:
    for i in range(a):
        for k in range(b):
            diagonals = i + k + 1
            old_diagonals = diagonals - 1
            for h in range(1, old_diagonals + 1):
                if h <= a:
                    total += h
                elif h > b:
                    total += b - (h - b)
            if diagonals <= b:
                total += i + 1
            elif diagonals > b:
                total += (i + 1) - (diagonals - b)
            elem.append(total)
            total = 0
        matrix.append(elem)
        elem = []

for i in range(a):
    print(*matrix[i])
    
    

n, m = [int(i) for  i in input().split()]           #Получаем размер матрицы
next_number = iter(range(1, n * m + 1))             #Делаем генератор следующего числа в матрице
res = [[0 for j in range(m)] for i in range(n)]     #Создаем пустую матрицу для заполнения
list_step = []                                      #Подготавливаем пустой список диаганалей

if 1 in [n, m]:                                     #Делаем генерацию всех диаганалей 
    list_step.extend([1] * max(n, m))               #Заполняем для матриц где одна из сторон равна 1
else:
    step = min(n, m)                                #Определяем максимальный шаг(диаганаль) 
    list_step.extend([i for i in range(1, step + 1)])   #Заполняем список диагаей приростающими значениями
    if n - m:
        list_step.extend([step for _ in range(m - n)])  #Добавляем повторяющие диаганали, вслучии если матрица "широкая"
    if n - step - 1:
        list_step.extend([step for _ in range(n - step)])   #Добавляем повторяющие диаганали, вслучии если матрица "длинная"
    list_step.extend([step - i if  step - i > 0 else 1 for i in range(1, step)])   #Заполняем список диагаей спадающими значениями 

for d in range(len(list_step)):                     #Делаем проход по диаганалям
    index_j = d if d < m else m - 1                 #Вычисляем координаты i для начала заполнения
    index_i = 0 if d < m else d - m + 1             #ВЫчисляем координаты j для начала заполнения
    for i in range(list_step[d]):                   #Берем диаганаль и начинаем проход по ней
        res[index_i + i][index_j - i] = str(next(next_number)).ljust(3) #Заполняем конкретную точку на диаганали следующим значением

for item in res:    #Типовой вывод матрицы, тута взяли строку
    print(*item)    #Выводим строку
    

[print(*[str((r * (r + 1) - (r > n) * (r - n) * (r - n + 1) - (r >= m) * (r - m + 1) * (r - m + 2)) // 2 + i + 1).ljust(2) for r in range(i, i + m)]) for n, m in [map(int, input().split())] for i in range(n)]



def print_matrix(a):
    for row in a:
        print(*row)

def fill_line(a, irow, icol, k):
    """заполняем одну диагональную линию сверху вниз от (irow,icol) начиная с числа k,
    возвращаем k для следующей клетки
    """
    m = len(a)
    n = len(a[0])
    while 0 <= irow < m and 0 <= icol < n:
        # print(f'k={k} irow={irow} icol={icol}')
        a[irow][icol] = k
        k += 1
        irow += 1
        icol -= 1
    return k

def fill_matrix(a):
    k = 1
    for j in range(len(a[0])):
        k = fill_line(a, 0, j, k)
    j = len(a[0]) - 1
    for i in range(1, len(a)):
        k = fill_line(a, i, j, k)
    
rows, cols = map(int, input().split())
a = [[0]*cols for _ in range(rows)] 
#k = fill_line(a, 0, 0, 1)

fill_matrix(a)
print_matrix(a)



import numpy as np

n, m = [int(_) for _ in input().split()]
matrix = np.zeros((n, m), dtype= int)
value = 1
for j in range(n + m - 1):
    for i in range(j + 1):
        if (i < n) and (j - i < m):
            matrix[i][j - i] = value
            value += 1

for row in matrix:
    print(*row)
'''