n, k = int(input()), int(input())
#s = list(range(1, n + 1))
s = [i for i in range(1, n + 1)]
while len(s) > 1:
    for q in range(0, k - 1):
      s.append(s[q])
    del s[:k]

print(s[0])
print(*s)

'''
n = int(input())
k = int(input())

res = 0
for i in range(1, n+1):
    res = (res + k) % i
print(res + 1)



def josephus_task(n, k):
    soldiers = list(range(1, n + 1))
    index = 0
    while len(soldiers) > 1:
        index = (index + k - 1) % len(soldiers)
        soldiers.pop(index)
    return soldiers[0]

n = int(input())
k = int(input())
print(josephus_task(n, k))

def josephus(n, k):
  if n == 1:
      return 1
  else:
      return (josephus(n - 1, k) + k - 1) % n + 1

# Считываем значения n и k
# n, k = map(int, input().split())
n = int(input("Введите количество человек: "))
k = int(input("Введите число, через которое следует исключать: "))

# Выводим номер последнего оставшегося узника
print(josephus(n, k))


n = int(input("Введите количество человек: "))
k = int(input("Введите число, через которое следует исключать: "))

people = list(range(1, n + 1))  # Создаем список людей с номерами от 1 до n

# Итеративно удаляем каждого k-ого человека из списка
index = 0
while len(people) > 1:
    index = (index + k - 1) % len(people)  # Находим индекс человека для удаления
    people.pop(index)

print("Последний выживший человек:", people[0])

n = int(input())
k = int(input())

# создаем список людей, где каждый человек – просто номер
people = list(range(1, n + 1))
# переменная для текущей позиции "считалки"
cur = 0

# пока у нас больше одного человека
while len(people) > 1:
    # начинаем считалку от текущей позиции cur, постоянно увеличивая ее
    for _ in range(k - 1):
        cur += 1
        # если считалка переваливает за последнего человека,
        # то ставим ее на первого человека
        if cur == len(people):
            cur = 0

    people.pop(cur)
    # если удалили последнего человека,
    # то считалку ставим на первого человека
    if cur == len(people):
        cur = 0

# выводим единственного оставшегося человека
print(people[0])

n = int(input())
k = int(input())

# создаем список людей, где каждый человек – просто номер
people = list(range(1, n + 1))
# переменная для текущей позиции "считалки"
cur = 0

# пока у нас больше одного человека
while len(people) > 1:
    # начинаем считалку от текущей позиции cur, постоянно увеличивая ее
    for _ in range(k - 1):
        cur += 1
        # если считалка переваливает за последнего человека,
        # то ставим ее на первого человека
        if cur == len(people):
            cur = 0

    people.pop(cur)
    # если удалили последнего человека,
    # то считалку ставим на первого человека
    if cur == len(people):
        cur = 0

# выводим единственного оставшегося человека
print(people[0])

dx, n, k = 0, int(input()), int(input()) - 1
nums = list(range(1, n + 1))
while len(nums) > 1:
    idx = (idx + k) % len(nums)
    nums.pop(idx)
print(nums[0])

def joseph(n, k):
    return 1 if n == 1 else (joseph(n - 1, k) + k - 1) % n + 1

print(joseph(int(input()), int(input())))

#Ввод параметров:
n = int(input())
k = int(input())

#Создание массива номеров, из которого потом будем выкидывать элементы.
line = [i for i in range(1, n+1)]


# Нам нужно отсчитать k элементов по массиву из n первых натуральных чисел. Затем выкинуть 
# элемент, на котором будет остановлен счет и сдвинуть весь массив так, чтобы первым стал
# следующий после выкинутого, а те элементы, что были до него, перешли в конец. А дальше 
# все просто повторяется, пока в массиве не останется один элемент - это и будет искомый номер 
# Для этого сначала берем остаток от деления k на длину массива (не просто k - потому что k
# может быть больше длины массива). Если он больше 0, то выкидываем элемент массива с номером,
# равным этому остатку, уменьшенному на единицу (нумерация от нуля), если же он равен нулю,
# то это означает, что надо просто выкинуть последний элемент, а массив никуда не сдвигать.
# Оставшийся в результате массив из одного элемента и дает нужный номер.

while(len(line) > 1):
    num = k % len(line)
    if num > 0:
        pos = num - 1
        line.pop(pos)
        line = line[pos:] + line[:pos]
    else:
        line.pop(-1)

print(line[0])

n, k = [i + 1 for i in range(int(input()))], int(input())
c = 0
while len(n) > 1:
    c += (k - 1) 
    c %= len(n)
    n.pop(c)
print(*n)

import collections
n = [i for i in range(int(input()))]
m = int(input())
deq = collections.deque(enumerate(n))
while len(deq) > 1:
 deq.rotate(-m)
 deq.pop()
print(deq[0][0]+1)
'''