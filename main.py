n = int(input())
matrix = []

while len(matrix) < n:
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(n):
    average = sum(matrix[i]) / n
    count = sum(1 for elem in matrix[i] if elem > average)
    print(count)
    

