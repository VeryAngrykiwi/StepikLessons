I = 0
II = 0
III = 0
IV = 0
for _ in range(int(input())):
    s=input().split()
    if int(s[0])>0:
      if int(s[1]) > 0:
        I += 1
      elif int(s[1]) < 0:
        IV += 1
    elif int(s[0])< 0:
      if int(s[1]) > 0:
        II += 1
      elif int(s[1]) < 0:
        III += 1

print(f'Первая четверть: {I}\nВторая четверть: {II}\nТретья четверть: {III}\nЧетвертая четверть: {IV}')

'''
points_count = int(input())
q1 = q2 = q3 = q4 = 0

for _ in range(points_count):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        q1 += 1
    elif x < 0 and y > 0:
        q2 += 1
    elif x < 0 and y < 0:
        q3 += 1
    elif x > 0 and y < 0:
        q4 += 1

print(f'Первая четверть: {q1}\nВторая четверть: {q2}\nТретья четверть: {q3}\nЧетвертая четверть: {q4}')

n = int(input())
count = [0, 0, 0, 0]
names = ['Первая четверть:', 'Вторая четверть:', 
         'Третья четверть:', 'Четвертая четверть:']

for _ in range(n):
    x, y = [int(num) for num in input().split()]
    if x > 0 and y > 0:
        count[0] += 1
    elif x < 0 and y > 0:
        count[1] += 1
    elif x < 0 and y < 0:
        count[2] += 1
    elif x > 0 and y < 0:
        count[3] += 1

for i in range(4):
    print(names[i], count[i])

c = 4 * [0] + [int(input())]
for _ in range(c[4]):
    x, y = map(int, input().split())
    c[x < 0 if y > 0 else 2 + (x > 0)] += not 0 in [x, y]
[print(f"{['Первая', 'Вторая', 'Третья', 'Четвертая'][i]} четверть: {c[i]}") for i in range(4)]

a_1, a_2, a_3, a_4 = 0, 0, 0, 0
for _ in range(int(input())):
    x, y = input().split()
    if int(x) > 0 and int(y) >0:
        a_1 +=1
    elif int(x) < 0 and int(y) >0:
        a_2 += 1
    elif int(x) < 0 and int(y) < 0 :
        a_3 += 1
    elif int(x)> 0 and int(y) < 0 : 
        a_4 +=1

print(f'Первая четверть: {a_1}', f'Вторая четверть: {a_2}', f'Третья четверть: {a_3}', f'Четвертая четверть: {a_4}', sep='\n')

n = int(input())

results = []

for _ in range(n):
    x, y = map(int, input().split())
    if x and y != 0:
        results.append([['I', 'II'],  ['IV', 'III']][y < 0][x < 0])

print('Первая четверть:', results.count('I'))
print('Вторая четверть:', results.count('II'))
print('Третья четверть:', results.count('III'))
print('Четвертая четверть:', results.count('IV'))

cnt = [0] * 4
quarters = ('Первая', 'Вторая', 'Третья', 'Четвертая')

for _ in range(int(input())):
    x, y = map(int, input().split())
    cnt[(x * y < 0) + 2 * (y < 0)] += bool(x * y)

print(*(f'{q} четверть: {c}' for q, c in zip(quarters, cnt)), sep='\n')

m = []
ch = ['Первая', 'Вторая', 'Третья', 'Четвертая', 11, 9, -11, -9]

for _ in range(int(input())):
    x, y = map(int, input().split())
    if 0 not in [x, y]:
        m.append([-1, 1][x > 0] + [-10, 10][y > 0])

for i in range(4):
    print(ch[i] + ' четверть:', m.count(ch[i + 4]))

import re
coordinates = str([input() for _ in range(int(input()))])
print('Первая четверть:', len(re.findall(r'\b(?<!-)[1-9][0-9]* [1-9][0-9]*', coordinates)))
print('Вторая четверть:', len(re.findall(r'-\b[1-9][0-9]* [1-9][0-9]*', coordinates)))
print('Третья четверть:', len(re.findall(r'-\b[1-9][0-9]* -[1-9][0-9]*', coordinates)))
print('Четвертая четверть:', len(re.findall(r'\b(?<!-)[1-9][0-9]* -[1-9][0-9]*', coordinates)))
'''