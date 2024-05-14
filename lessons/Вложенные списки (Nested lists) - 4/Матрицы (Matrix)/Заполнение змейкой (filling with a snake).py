#Вариант 1:
n, m = map(int, input().split())
g = (i for i in range(1, n*m+1))
a = [[str(g.__next__()).ljust(2) for _ in range(m)] for _ in range(n)]

for i in a:
    if a.index(i) % 2 != 0:
        i.reverse()
#        k = ' '.join(map(str, i))
        print(*i)
    else:
  #      k = ' '.join(map(str, i))
        print(*i)

#Вариант 2:
n, m = map(int, input().split())
mtx = [[0 for i in range(m)] for q in range(n)]

for i in range(n):
    for j in range(m):
        mtx[i][j] = i * m + j + 1

for i in range(len(mtx)):
    if i % 2:
        mtx[i].reverse()

for i in range(n):
    for j in range(m):
        print(str(mtx[i][j]).ljust(2), end=' ')
    print()


'''
n, m = map(int, input().split())
a = [[str(j + i*m).ljust(3) for j in range(1, m+1)][::(-1)**i] for i in range(n)]
for el in a:
  print(*el)



n, m = map(int, input().split())
for i in range(n):
    for j in range(m):
        print(str(i * m + j + 1).ljust(3) if i % 2 == 0 else str((i + 1) * m - j).ljust(3), end=' ')
    print()



a, b = map(int, input().split())

for i in range(a):
    print(*sorted(list(range(i*b + 1, i*b + b + 1)), reverse=i%2))
    

(lambda n, m : [print(*range(1 + i * m, 1 + m * (i + 1))[::[1, -1][i % 2 == 1]]) for i in range(n)])(*[int(num) for num in input().split()])
'''