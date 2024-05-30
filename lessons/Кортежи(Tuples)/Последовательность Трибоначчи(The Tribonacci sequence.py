n = int(input())
x1, x2, x3 = 1, 1, 1
for i in range(n):
    print(x1, end=' ')
    x1, x2, x3 = x2, x3, x1 + x2 +x3

'''
n = int(input())
t1 = t2 = t3 = 1
for _ in range(n):
    print(t1, end=' ')
    t1, t2, t3 = t2, t3, t1 + t2 + t3


   
n = int(input())

lst = [1, 1, 1]

for i in range(n-3):
    lst.append(sum(lst[-3:]))

print(*lst[:n])



def dofigacci(n, lensum):
    ntuple = (1,)*lensum
    for _ in range(min(lensum, n)):
        print(1, end=' ')
    for _ in range(n-lensum):
        ntuple = *ntuple[1:], sum(ntuple)
        print(ntuple[-1], end=' ')

n = int(input())
dofigacci(n, 3)



tt=(1,1,1)
n=int(input())

for i in range(3,n):
  tt+=(sum(tt[i-3:i]),)
print (*tt[:n])



z = []
[z.append(1 if i < 3 else sum(z[i-3:i])) for i in range(int(input()))]
print(*z)



from functools import lru_cache

@lru_cache(100)
def tribo(n):
    if n < 3:
        return 1
    else:
        return tribo(n-1) + tribo(n-2) + tribo(n-3)

for i in range(int(input())):
    print(tribo(i), end=' ')
'''