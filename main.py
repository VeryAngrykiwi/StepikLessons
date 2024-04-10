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
