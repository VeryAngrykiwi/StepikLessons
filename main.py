n = int(input())

mtx = [] #матрица - пустой список 
for _ in range(n): #цикл наполнения матрицы
  tmp = [0 for _ in range(n)]
  mtx.append(tmp)


for i in range(n): 
  for q in range(n):
    if i == q:
      mtx[i][q] = 1
    elif i == n-1-q:
      mtx[i][q] = 1

[print(*row) for row in mtx]
print()
[print(*mtx[i]) for i in range(n)]




