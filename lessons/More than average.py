n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

for row in matrix:
    average = sum(row) / n
    count = sum(1 for elem in row if elem > average)
    print(count)

'''
n = int(input())
matrix = []
for k in range(n):
    tmp = [int(x) for x in input().split()]
    matrix.append(tmp)

for i in range(n):
  sum = 0
  count = 0
  for q in range(n):
    sum +=matrix[i][q]
  for r in range(n):
    if matrix[i][r] > sum/n:
      count +=1
  print(count)


for _ in range(int(input())):
  lst = list(map(int, input().split()))
  avg = sum(lst) / len(lst)
  print(sum(i > avg for i in lst))


matrix = [[int(_) for _ in input().split()] for _ in range(int(input()))]
print(*[len([_ for _ in r if _ > sum(r) / len(r)]) for r in matrix], sep='\n')


(lambda n: [print(len(list(filter(lambda y: y > sum(i) / n, i)))) for i in [list(map(int, input().split())) for __ in range(n)]])(int(input()))



n=int(input())
matrix=[[int(i) for i in input().split()] for _ in range(n)]
for i in range(n): 
    print(sum(matrix[i][j]>sum(matrix[i])/n for j in range(n)))


print(*[len(sub) for sub in[[1 for i in j if i > sum(j)/len(j)]for j in [list(map(int, input().split()))for _ in range(int(input()))]]],sep='\n')


n = int(input())
matrix = []

while len(matrix) < n:
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(n):
    average = sum(matrix[i]) / n
    count = sum(1 for elem in matrix[i] if elem > average)
    print(count)
'''

