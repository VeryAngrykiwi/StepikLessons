n = int(input())
students = [list(input().split()) for _ in range(n)]

for row in students:
  print(*row)
print()
for i in range(n):
  if int(students[i][1]) > 3:
    print(*students[i])