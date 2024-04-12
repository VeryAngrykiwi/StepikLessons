virus = 'anton'
for i in range(1, int(input()) + 1):
  s = input()
  res = ''
  for x in virus:
    if x in s:
      res += x
      s = s[s.find(x):]
  if res == virus:
    print(i, end= ' ')

'''
import re

n = int(input())  # количество холодильников
infected_fridges = []  # список зараженных холодильников

# Читаем данные о холодильниках
for i in range(n):
    fridge_data = input()
    if re.search(r'a.*n.*t.*o.*n', fridge_data):
        infected_fridges.append(i + 1)  # добавляем номер холодильника в список

# Выводим номера зараженных холодильников
if infected_fridges:
    print(*infected_fridges)


n = int(input())
for i in range(n):
    seq = ["a", "n", "t", "o", "n"]
    s = list(input())

    while seq and s:  # пока у нас непустые список из букв строки и список слова "anton"
        if seq[0] == s[0]:  # если буквы равны, то вырываем и там, и там
            seq.pop(0)
            s.pop(0)
        else:  # иначе вырываем только из списка букв строки
            s.pop(0)

    # если список букв слова "anton" пустой, значит вырвали все буквы,
    # значит в строке встретились все эти буквы в нужном нам порядке
    if not seq:
        print(i + 1, end=" ")


for i in range(int(input())):
  s, virus, x  = input(), 'anton', 0
  for sym in s:
      if sym == virus[x]:
          x += 1
      if x == 5:
          print(i + 1, end=' ')
          break    

import re
num = int(input())
for i in range(num):
    if re.search(r'.*a.*n.*t.*o.*n', input()):
        print(i + 1, end=' ')


print(*[k + 1 for k in range(int(input())) if __import__('re').match(".*a.*n.*t.*o.*n.*", input())])


sp = []
for i in range(int(input())):
    s = input()
    if s.rfind('a', 0, s.rfind('n', 1, s.rfind('t', 2, s.rfind('o', 3, s.rfind('n', 4) + 1) + 1) + 1) + 1) > -1:
        sp.append(i + 1)
print(*sp)
'''
