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
