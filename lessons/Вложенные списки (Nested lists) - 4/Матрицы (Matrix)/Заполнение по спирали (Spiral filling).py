#Вариант 1
# вход строка чисел
s = input().split()

# считывание строки чисел
n, m = int(s[0]), int(s[1])

# создание пустой матрицы
mtx = []

# построение матрицы методом append
for _ in range(n):
    tmp = [0 for e in range(m)]
    mtx.append(tmp)

# создание переменных для указания направления движения чисел
x, y = 0, 0
dx, dy = 0, 1  # шаг матрицы, направление
mtx[0][0] = 1  # начало матрицы
count = 2

# наполнение матрицы цикл while
while count <= n * m:  #длина матрицы
    if 0 <= x + dx <= n - 1 and 0 <= y + dy <= m - 1 and mtx[x + dx][y + dy] == 0:
        mtx[x + dx][y + dy] = count
        count += 1
        x += dx
        y += dy
    else:
        if dy == 1:
            dy = 0
            dx = 1
        elif dx == 1:
            dx = 0
            dy = -1
        elif dy == -1:
            dy = 0
            dx = -1
        elif dx == -1:
            dx = 0
            dy = 1
#    print(mtx)


# печать матрицы с отступами, методом str.
for i in range(n):
    for j in range(m):
        print(str(mtx[i][j]).ljust(2), end=' ')
    print()


'''
n, m = [int(i) for i in input().split()]

matrix = [[0] * m for _ in range(n)]
counter = 1
rows_passed, columns_passed = 0, 0
current_row, current_column = 0, 0

for k in range(n * m):
    if counter == n * m + 1:
        break
    direction = k % 4
    if direction == 0:
        for j in range(columns_passed, m - columns_passed):
            matrix[current_row][j] = counter
            counter += 1
        current_column = j
        rows_passed += 1
    elif direction == 1:
        for i in range(rows_passed, n - rows_passed + 1):
            matrix[i][current_column] = counter
            counter += 1
        current_row = i
        columns_passed += 1
    elif direction == 2:
        for j in range(current_column - 1, columns_passed - 2, -1):
            matrix[current_row][j] = counter 
            counter += 1
        current_column = j
    elif direction == 3:
        for i in range(current_row - 1, rows_passed - 1, -1):
            matrix[i][current_column] = counter
            counter += 1
        current_row = i 
        
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()



n, m = map(int, input().split())

i = 0
j = 0
cnt = 1

a = [[0 for _ in range(m)] for _ in range(n)]

while cnt < m * n:
    while j < m - 1 and a[i][j + 1] == 0:
        a[i][j] = cnt
        j += 1
        cnt += 1

    while i < n - 1 and a[i + 1][j] == 0:
        a[i][j] = cnt
        i += 1
        cnt += 1

    while j > 0 and a[i][j - 1] == 0:
        a[i][j] = cnt
        j -= 1
        cnt += 1

    while i > 0 and a[i - 1][j] == 0:
        a[i][j] = cnt
        i -= 1
        cnt += 1

a[i][j] = cnt

for i in range(n):
    for j in range(m):
        print(str(a[i][j]).ljust(3), end=' ')
    print()
    


n, m = map(int, input().split())
a = [[0] * m for _ in range(n)]
dr, dc, r, c = 0, 1, 0, 0

for cnt in range(1, n * m + 1):
    a[r][c] = cnt
    
    if a[(r + dr) % n][(c + dc) % m]:
        dr, dc = dc, -dr

    r += dr
    c += dc    
    
for row in a:
    print(*(f'{e:<3}' for e in row), sep='')
    


n, m = map(int, input().split())
i = 1; j = 0; c = 0
a = [[0] * (100) for _ in range(100)]

while c < m * n:
    while a[i][j+1] == 0 and j < m: a[i][j+1] = c+1; j += 1; c += 1
    while a[i+1][j] == 0 and i < n: a[i+1][j] = c+1; i += 1; c += 1
    while a[i][j-1] == 0 and j > 1: a[i][j-1] = c+1; j -= 1; c += 1
    while a[i-1][j] == 0 and i > 1: a[i-1][j] = c+1; i -= 1; c += 1

for i in range(1, n+1):
    for j in range(1, m+1):
        print(str(a[i][j]).ljust(3), end=' ')
    print()



# Принимаем параметры матрицы
# Альтернативный код: n, m = [int(i) for i in input().split()]
n, m = map(int, input().split())

# Создаем нулевую матрицу размером 'n x m'
matrix = [[0] * m for _ in range(n)]

# Задаем параметры направления смещения
# row_dir - смещение по строкам
# col_dir - смещение по столбцам
# Как видно в нашем случае мы двинемся горизонтально вправо
row_dir, col_dir = 0, 1

# Задаем координаты стартовой ячейки
row, column = 0, 0

# Цикл-счетчик порядкового номера от 1 до n * m
for counter in range(1, n * m + 1):
    # Присваиваем текущей ячейке номер счетчика
    matrix[row][column] = counter
    # Проверяем, не пора ли сделать поворот?
    # Проблема выхода за пределы матрицы решается делением с остатком
    if matrix[(row + row_dir) % n][(column + col_dir) % m]:
        # Поворачиваем направление смещения по часовой стрелке на 90 градусов
        row_dir, col_dir = col_dir, -row_dir
    # Задаем координаты следующей ячейки в соответствии с направлением смещения
    row += row_dir
    column += col_dir

# Распечатываем заполненную матрицу
for row in matrix:
    # переводим матрицу в строковый формат для эстетики отображения
    print(*(f'{e:<3}' for e in row), sep='')
    


#----------ВВОД----------
st, cl = [int(i) for i in input().split()]
matrix = [[0] * cl for col in range(st)]


#----------РЕШЕНИЕ----------
matrix[0] = [i for i in range(1, cl+1)]
y, x = 0, cl-1  # координаты на начало части цикла
my_flag = 1  # ГОРЖУСЬ этой переменной ))) избавились от 2 циклов, и с ее помощью указываем: прибавлять или убавлять координату
size = 1  # размерность, на сколько уменьшить длину прохода
score = cl + 1  # текущая цифра для вставки

while score <= st * cl:
    # двигаемся по вертикали
    for _ in range(st - size):
        y += my_flag
        matrix[y][x] = score
        score += 1

    my_flag *= -1

    # двигаемся по горизонтали
    for _ in range(cl - size):
        x += my_flag
        matrix[y][x] = score
        score += 1

    size += 1

#----------ВЫВОД----------
for row in range(st):
    for col in range(cl):
        print(str(matrix[row][col]).ljust(3), end='')
    print()
'''