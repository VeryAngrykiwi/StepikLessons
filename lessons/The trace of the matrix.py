n = int(input())
matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

trace = sum(matrix[i][i] for i in range(n))
print(trace)

'''
n = int(input())
matrix = []

for k in range(n):
  tmp = [int(x) for x in input().split()]
  matrix.append(tmp)

sum = 0
for i in range(n):
  for j in range(n):
    if i == j:
      sum += matrix[i][j]
print(sum)


n = int(input())
sm = 0

for i in range(n):
    cur_seq = input().split()
    sm += int(cur_seq[i])

print(sm)


res = 0
for i in range(int(input())):
    res += int(input().split()[i])
print(res)


print(sum(int(input().split()[i]) for i in range(int(input()))))


n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
print(sum([matrix[i][i] for i in range(n)]))


# Ввод пользователя
n = int(input())
# Создание матрицы
matrix = [input().split() for i in range(n)]
# Вывод суммы главной диагонали
print(sum([int(matrix[i][i]) for i in range(n)]))


matrix = [input().split() for __ in range(int(input()))]
print(sum([int(matrix[i][i]) for i in range(len(matrix))]))


from numpy import array, diag

arr = array([list(map(int, input().split())) for _ in range(int(input()))])
print(sum(diag(arr)))


(lambda L: print(sum(L[1::L[0]+1])))([*map(int, open(0).read().split())])
'''