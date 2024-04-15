n = int(input())
mtx = [input().split() for _ in range(n)]

mtx.reverse()

[print(*row) for row in mtx]

'''
n = int(input())
matrix = [input().split() for _ in range(n)]

for i in range(n // 2):
    matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]

for row in matrix:
    print(*row)



n = int(input())

matrix = [[int(item) for item in input().split()] for _ in range(n)]
matrix.reverse()

for row in matrix:
    print(*row)


n = int(input())

res = [[int(x) for x in input().split()] for _ in range(n)]

for j in range(n - 1, -1, -1):
    print(*res[j])


[print(*row) for arr in [[input().split() for _ in range(int(input()))]] for row in arr[::-1]]



print('\n'.join(reversed([input() for _ in range(int(input()))])))



n = int(input())
mat = [input().split() for _ in range(n)]
for i in range(n):
    print(*mat[n-1-i])



[print(a) for a in [input() for _ in range(int(input()))][::-1]]
'''