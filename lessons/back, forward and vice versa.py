x = [int(i) for i in input().split()]
for j in range(0, len(x) -1, 2):
  x[j], x[j + 1] = x[j + 1], x[j]
print(*x)


'''
# Принимаем входные данные
numbers = list(map(int, input().split()))

# Меняем местами соседние элементы списка
for i in range(0, len(numbers) - 1, 2):
    numbers[i], numbers[i+1] = numbers[i+1], numbers[i]

# Выводим измененный список
print(*numbers)


numbers = input().split()

for i in range(0, len(numbers) - 1, 2):
    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

print(*numbers)

s = list(map(int, input().split()))
s[:-1:2], s[1::2] = s[1::2], s[:-1:2]
print(*s)

d = input().split()

d[:-1:2], d[1::2] = d[1::2], d[:-1:2]

print(*d)

s = input().split()
new_s = []
for i in s:
    new_s.append(i)
if len(s) % 2 == 0:
    for i in range(len(s)):
        if i % 2 == 0:
            new_s[i] = s[i + 1]
        else:
            new_s[i] = s[i - 1] 
else:
    for i in range(len(s) - 1):
        if i % 2 == 0:
            new_s[i] = s[i + 1]
        else:
            new_s[i] = s[i - 1]

print(' '.join(new_s))

m = [int(i) for i in input().split()]
for i in range(0,len(m), 2):
    try:
        m[i], m[i+1] = m[i+1], m[i]
    except IndexError:
        pass
print(*m)

print(*list(__import__('itertools').chain(*(lambda a: [(a[i], a[i-1]) for i in range(1, len(a), 2)] + a[len(a)//2*2:])(input().split()))))

print(*[l[i + (i < len(l) >> 1 << 1) * (-1) ** i] for l in [list(map(int, input().split()))] for i in range(len(l))])

lst = input().split()
lst_1 = []
for i in range(len(lst)):
    if len(lst) >= 2:
        lst_1.append(lst[1])
        lst_1.append(lst[0])
        del lst[1]
        del lst[0]
    if len(lst) == 1:
        lst_1.append(lst[0])
        del lst[0]
        break
print(*lst_1)
'''
