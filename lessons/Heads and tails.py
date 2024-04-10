print(max([len(i) for i in input().split('О')]))


'''
s = input()
seq = s.split("О")  # убираем всех орлов и группируем решек

mx = 0  # максимум подряд идущих решек
for el in seq:
    mx = max(mx, el.count("Р"))

print(mx)


def max_consecutive_tails(text) -> str:
  max_count = 0
  count = 0

  for char in text:
      if char == 'Р':
          count += 1
          max_count = max(max_count, count)
      else:
          count = 0

  return max_count

text = input()
result = max_consecutive_tails(text)
print(result)


s = input().split('О')
print(len(max(s)))


s = input().split('О')
print(len(max(s)))


res = input()
tmp = ''
while tmp in res:
    tmp += 'Р'
print(len(tmp) - 1)


a = input()
counter = 0
counter_max = 0
for i in range(len(a) - 1):
    if a[i] == 'Р' and a[i] == a[i + 1]:
        counter += 1
        if counter > counter_max:
            counter_max = counter
    elif a[i] != a[i + 1]:
        counter = 0

if 'Р' not in a:
    print(0)
else:
    print(counter_max + 1)


n = input()
v = [i for i in n]
v.append('О')
count = 1
w = []
for i in range(len(v) - 1):
  if v[i] == 'Р' and v[i] == v[i + 1]:
    count += 1
  elif v[i + 1] != 'Р' or (v[i + 1] == 'Р' and v[-1] == v[i + 1]):
    w.append(count)
    count = 1
if 'Р' not in n:
  print('0')    
else:
  print(max(w))
'''
