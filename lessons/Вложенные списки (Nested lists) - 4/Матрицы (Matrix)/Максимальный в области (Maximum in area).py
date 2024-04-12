#maximum in area 1

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

#maximum in area 2

n = int(input())
matrix = []
for k in range(n):
    tmp = [int(x) for x in input().split()]
    matrix.append(tmp)

max = matrix[0][0]

for i in range(n):
    for j in range(n):
        if (i >= j and i <= n - 1 - j or i <= j and i >= n - 1 - j) and matrix[i][j] > max:
            max = matrix[i][j]

print(max)

'''
n = int(input())
matrix = []

for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)

largest = matrix[0][0]

for i in range(n):
    for j in range(n):
        if (i >= j and i + j + 1 <= n) or (i <= j and i + j + 1 >= n):
            if matrix[i][j] > largest:
                largest = matrix[i][j]

print(largest)



n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
print(max(max(m[i][j], m[i][~j], m[~i][j], m[~i][~j]) for i in range(n // 2 + 1) for j in range(i + 1)))



maximum = []
m = int(input())
for i in range(m):
    my_string = [int(i) for i in input().split()]
    maximum.extend(my_string[:min(i + 1, m - i)])
    maximum.extend(my_string[max(-i - 1, i - m):])
print(max(maximum))



# обработка вводимых данных и преобразование их в квадратную матрицу
def matrix_sqr():
    matrix = [input().split() for _ in range(int(input()))]
    return matrix
# нахождение эл-тов заштрихованной части квадратной матрицы
def stroke_matrix_sqr(matrix): 
    nums = []
    # добавляем эл-ты главной и побочной диагоналей
    for i in range(len(matrix)):
        nums.append(int(matrix[i][i]))
        nums.append(int(matrix[i][len(matrix)-i-1]))
    # добавляем заштрихованные части матрицы
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            if (j<i and i+j+1< len(matrix)) or (i<j and i+j+1> len(matrix)):
                nums.append (int(matrix[i][j]))
    # выводим максимум из заштрихованной части            
    return max(nums)

matrix = matrix_sqr()
print (stroke_matrix_sqr(matrix))


n = int(input())
a = [[*map(int, input().split())] for _ in range(n)]
print(max(max(a[i][j], a[i][~j]) for j in range(n // 2) for i in range(j, n - j)))


размерность = int(input())
диагонали = tuple(range(1,размерность//2+1))
диагонали = диагонали + ((размерность//2+1,) if размерность%2 else ()) + диагонали[::-1]

взять_линию = lambda: (*map(int, input().split()),)
матрица = *(взять_линию() for _ in range(размерность)),

бабочка = []
for позиция, линия in zip(диагонали, матрица):    
    убрать = slice(позиция, -позиция)
    линия = list(линия)
    линия[убрать] = []

    добавить = slice(len(бабочка),0)
    бабочка[добавить] = линия

print( max(бабочка) )
'''