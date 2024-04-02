inp = input().split()
out = [[]]

for i in range(len(inp)):
  for j in range(len(inp) - i):
    out.append(inp[j:j + i + 1])
print(out)

'''
# неверно, нравится.
from itertools import combinations 

def sub_lists(lst):
    subs = []
    for i in range(len(lst) + 1):
        temp_subs = [list(x) for x in combinations(lst, i)]
        subs.extend(temp_subs)
    return subs

lst = input().split()
res = sub_lists(lst)
print(res)

#верно.
input_data = input().split()
# сохраняем сюда длину входного списка
n = len(input_data)

result = [[]]
for size in range(1, n + 1):
    # подсписок при проходе с захватом size элементов
    cur_seq = []
    for i in range(n - size + 1):
        cur_seq.append(input_data[i:i + size])

    result.extend(cur_seq)

print(result)


some_string = input()
some_list = some_string.split()
some_string = some_string.replace(' ', '')
final = [[]]
counter = 1
for i in range(len(some_list)):
  tmp = some_string

  for j in range(len(some_list) - i):
    a = tmp[:counter]
    final.append(a)
    tmp = tmp.replace(tmp[0], '', 1)

  counter += 1
  #print(final)
for i in range(len(final)):
  final[i] = list(final[i])
print(final)

print([[]] + [l[j:i + j + 1] for l in [input().split()] for i in range(len(l)) for j in range(len(l) - i)])


d = [[]]

def chunked(s, n):
    for i in range(len(s) - n + 1):
            d.append(s[i:i + n])
    return d

list1 = input().split()
for _ in range(1, len(list1)+1):
    chunked(list1, _)
print(d)


inp = input().split()
out = [[]]

i = 0
while i < len(inp):
    j = 0
    while j < len(inp) - i:
        out.append(inp[j:j + i + 1])
        j += 1
    i += 1

print(out)
'''