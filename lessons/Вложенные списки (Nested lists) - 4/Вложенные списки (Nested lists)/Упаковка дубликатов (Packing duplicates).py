s = input().split()
lst = [[s[0]]]
for i in range(1, len(s)):
  if s[i] == s[i - 1]:
    lst[-1].append(s[i])
  else:
    lst.append([s[i]])
print(lst)


'''
text = input().split()

result = []

for char in text:
    if not result or result[-1][-1] != char:
        result.append([char])
    else:
        result[-1].append(char)

print(result)


s = input().split()
# кидаем первый символ в наш список, также удалив его из входного списка
seq = [[s.pop(0)]]

for c in s:
    if c in seq[-1]:
        seq[-1].append(c)
    else:
        seq.append([c])

print(seq)


res = []

for el in input().split():
    if res and el in res[-1]:
        res[-1].append(el)
    else:
        res.append([el])

print(res)


spi = input().split()

new_spi = []
sp = []
i = 0 

while len(spi) != i:
    if i != len(spi) - 1:
        if spi[i] == spi[i + 1]:
            for j in range(i, len(spi)):
                if j != len(spi) - 1:
                    if spi[j] == spi[j + 1]:
                        sp.append(spi[j])
                    if spi[j] != spi[j + 1]:
                        if spi[j] == spi[j - 1]:
                            sp.append(spi[j])
                        new_spi.append(sp)
                        sp = []
                        i = j
                        break
                if j == len(spi) - 1:
                    if spi[j] == sp[-1]:
                        sp.append(spi[j])
                    new_spi.append(sp)
                    sp = []
                    i = j
                    break
        if len(spi) - 1 != i and len(new_spi) == 0:
            if spi[i] != spi[i + 1]:
                new_spi.append([spi[i]])
        elif len(spi) - 1 != i and spi[i] == new_spi[-1][-1] and len(sp) != 0:
            if spi[i] != spi[i + 1]:
                new_spi.append([spi[i]])
        elif len(spi) - 1 != i and spi[i] != new_spi[-1][-1]:
            if spi[i] != spi[i + 1]:
                new_spi.append([spi[i]])
    if i == len(spi) - 1 and len(sp) >= 1:
        if sp[0] == spi[i]:
            sp.append(spi[i])
            new_spi.append(sp)
        if sp[0] != spi[i]:
            new_spi.append(spi[i])
    if i == len(spi) - 1:
        if spi[i] != spi[i - 1]:
            new_spi.append([spi[i]])
    i = i + 1

print(new_spi)


res = []
a = input().split()
for i in a:
    res.append([i]) if not res or i not in res[-1] else res[-1].append(i)
print(res)


letters = [[letter] for letter in input().split()]

i = 1
while (i < len(letters)):
    if (letters[i][0] == letters[i - 1][0]):
        letters[i - 1].extend(letters.pop(i))
    else:
        i += 1

print(letters)


from itertools import groupby

s = input().split()
print(list(list(seq) for sym, seq in groupby(s)))


p, s = [], []
for i in input().split():
    if i in p:
        p += i
    else:
        p = [i]
        s += [p]
print(s)


res = []
[res.append([el]) if not res or el not in res[-1] else res[-1].append(el) for el in input().split()]
print(res)
'''
