n = int(input())
students = [list(input().split()) for _ in range(n)]

for row in students:
  print(*row)
print()
for i in range(n):
  if int(students[i][1]) > 3:
    print(*students[i])


'''
students = [tuple(input().split()) for _ in range(int(input()))]

for student in students:
    print(*student)

print()

for name, grade in students:
    if int(grade) > 3:
        print(name, grade)



pup = [input() for _ in range(int(input()))]
print(*pup, sep='\n')
print()
[print(x) for x in pup if int(x[-1]) > 3]



a = [input() for i in range(int(input()))]
print(*a, '', *[i for i in a if int(i[-1]) >= 4], sep='\n')



n = int(input())
pupil = tuple(input().split() for _ in range(n))
[print(*i) for i in pupil]
print()
[print(*i) for i in pupil if int(i[1]) > 3]



n = int(input())
s =[]
for i in range(n):
    s += [input().split()]
for c in s:
    print(*c)
print()
for c in s:
    if c[1] in '45':
        print(*c)



data = [input() for _ in range(int(input()))]
print(*data, sep='\n', end='\n\n')
print(*filter(lambda x: int(x.split()[1]) > 3, data), sep='\n')
'''