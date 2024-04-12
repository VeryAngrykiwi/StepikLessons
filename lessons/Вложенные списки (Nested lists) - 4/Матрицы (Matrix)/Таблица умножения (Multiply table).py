n, m = int(input()), int(input())
mult = []

for i in range(n):
    row = []
    for j in range(m):
        row.append(str(i * j).ljust(3))
    mult.append(row)
    print(*row)

'''
n, m = int(input()), int(input())
mult = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        mult[i][j] = i * j

for i in range(n):
    for j in range(m):
        print(str(mult[i][j]).ljust(3), end=' ')
    print()



m, n = int(input()), int(input())
mult =[[i*j for i in range(n)] for j in range(m)]

for i in range(m):
    for j in range(n):
        print(str(mult[i][j]).ljust(3), end=' ')
    print()



n, m = int(input()), int(input())
[print(*[str(i*j).ljust(3) for j in range(m)]) for i in range(n)]


[print(*[str(i * j).ljust(3) for j in d[1]]) for d in [[range(int(input())) for _ in 'nm']] for i in d[0]]


'''