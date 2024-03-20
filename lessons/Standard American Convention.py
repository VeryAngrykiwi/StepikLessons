n = input()
n = list(n)
for i in range(len(n)-3,0,-3):
    n.insert(i, ',')
print(''.join(n))

'''
def add_commas(n):
  num_with_commas = "{:,}".format(n)
  return num_with_commas

n = int(input("Enter a natural number: "))
result = add_commas(n)
print(result)

formatted_number = '{:,}'.format(n)
print(formatted_number)

def insert_commas(number):
number_str = str(number)
result = ''
for i, digit in enumerate(number_str[::-1]):
    if i % 3 == 0 and i != 0:
        result = ',' + result
    result = digit + result
return result

# Считываем число
n1 = int(input())

# Выводим число с запятыми
print(insert_commas(n1))

seq = list(input())
new_s = ""

while len(seq) >= 3:
    new_s += seq.pop(-1) + seq.pop(-1) + seq.pop(-1) + ","  # отрываем 3 последние цифры и ставим после них запятую

new_s += "".join(seq[::-1])  # обрабатываем цифры, которые могли остаться (их 1 или 2)

new_s = new_s[::-1]  # переворачивааем результат в первоначальный вид
new_s = new_s.lstrip(",")  # убираем лишнюю запятую

print(new_s)

s = input()
n = []

while len(s) > 0:
    n.append(s[-3:])
    s = s[:-3]

new_n = n[:: -1]
print(*new_n, sep = ',')

num = int(input())
print(f'{num:,}')

def comma(st):
    if len(st) < 4:
        return st
    return comma(st[:-3]) + ',' + st[-3:]

print(comma(input()))

a = str(input())
mas = []
newm =[]
k = 1
if len(a)> 3:
  for i in range(len(a)):
    mas.append(a[i])
  mas = mas[::-1]
  mas = [int(mas[i]) for i in range(len(mas))]
  for i in range (len(mas)):
    newm.append(str(mas[i]))
    if k > 2:
      newm.append(',')
      k = 0
    k += 1
  if len(a)%3 != 0:
    print(''.join(newm[::-1]))
  else:
    print(''.join(newm[-2::-1]))

else:
  print(a)

n, s = input()[::-1], ''
while len(n) > 3:
    s += n[:3] + ','
    n = n[3:]
s += n
print(s[::-1])
'''