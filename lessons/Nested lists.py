# Список по образцу 1 (The list is based on sample 1)
n = int(input())
ls = []
j = 0
i = 0

while j <= n:
  j += 1
  if ls == []:
    pass
  else:
    print(ls)
  while len(ls)< n:
    i += 1
    ls.append(i)

'''
n = int(input())
result = []

for _ in range(n):
    result.append(list(range(1, n + 1)))

print(*result, sep='\n')


n = int(input())
for _ in range(n):
    print(list(range(1, n + 1)))


[ [ print([i+1 for i in range(n)]) for _ in range(n) ] for n in [int(input())] ]


print(*[[i for i in range(1, n + 1)] for n in [int(input())] for _ in range(n)], sep='\n')


n = int(input())

for _ in range(n):
    elem = [i for i in range(1, n+1)]
    print(elem)


n = int(input())
print(*[[j for j in range(1, n + 1)] for _ in range(n)], sep='\n')
'''

# Список по образцу 2 (The list is based on sample 2)
n = int(input())
ls = []

i = 0

while len(ls)< n:
    i += 1
    ls.append(i)
    print(ls)

'''
n = int(input())
result = []

for i in range(1, n + 1):
    result.append(list(range(1, i + 1)))

print(*result, sep='\n')


[print(list(range(1, x + 2))) for x in range(int(input()))]


n = int(input())
for i in range(1, n + 1):
    print(list(range(1, i + 1)))


print(*[list(range(1, i + 1)) for i in range(1, int(input()) + 1)], sep="\n")


print(*(lambda n: [list(range(1, i + 1)) for i in range(1, n + 1)])(int(input())), sep="\n")
'''
