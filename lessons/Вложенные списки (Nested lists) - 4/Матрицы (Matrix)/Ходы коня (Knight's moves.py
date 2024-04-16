n = 8
mtx = [['.'] * n for _ in range(n)]
hv = input()
h = 'abcdefgh'.index(hv[0])
v = '87654321'.index(hv[1])
'''
for i in range(n):
  mtx[i][v] = '.'
  mtx[h][i] = '.'
'''
mtx[v][h] = 'N'
for i in range(n):
  for q in range(n):
    if (v-i)**2 + (h-q)**2 == 5:
      mtx[i][q] = '*'
[print(*row) for row in mtx]


'''
x, y = input()
n = 8
board = [['.'] * n for _ in range(n)]
x = ord(x) - 97
y = n - int(y)
board[y][x] = 'N'

for i in range(n):
    for j in range(n):
        if abs(y - i) * abs(x - j) == 2:
            board[i][j] = '*'

for row in board:
    print(*row)



x, y = list(input())
x, y = 'abcdefgh'.index(x), 8 - int(y)
arr = [['.*'[abs((x - j) * (y - i)) == 2] for j in range(8)] for i in range(8)]
arr[y][x] = 'N'
[print(*row) for row in arr]



vvod = input()
m, n, = vvod[0], int(vvod[1])
mass = [['.'] * 8 for i in range(8)]
i, j = 8 - n, ord(m) - 97
mass[i][j] = 'N'

if i <= 5 and j >= 1:
    mass[i + 2][j - 1] = '*'
if i <= 5 and j <= 6:
    mass[i + 2][j + 1] = '*'
if j >= 1 and i >= 2:
    mass[i - 2][j - 1] = '*'
if i >= 2 and j <= 6:
    mass[i - 2][j + 1] = '*'
if i >= 1 and j <= 5:
    mass[i - 1][j + 2] = '*'
if i <= 6 and j <= 5:
    mass[i + 1][j + 2] = '*'
if i >= 1 and j >= 2:
    mass[i - 1][j - 2] = '*'
if i <= 6 and j >= 2:
    mass[i + 1][j - 2] = '*'

for i in range(8):
    for j in range(8):
        print(mass[i][j], end=' ')
    print()



# put your python code here
# put your python code here
import copy
class matrix:
    def __init__(self, n = 0, m = 0, c=0):
        self.n = n
        self.m = m
        self.matrix = []
        for i in range(self.n):
            self.matrix.append([])
            for j in range(self.m):
                self.matrix[i].append(c)
    def minput(self):
        self.n = int(input())
        self.m = self.n
        for i in range(self.n):
            self.matrix.append([int(elem) for elem in input().split()])
    def mprint(self):            
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print(str(self.matrix[i][j]).ljust(2), end='')
            print()
    def transpose(self):
        new = matrix()
        new.matrix = []
        new.n = self.m
        new.m = self.n
        for i in range(self.m):
            new.matrix.append([])
            for j in range(self.n):
                new.matrix[i].append(self.matrix[j][i])
        return new
    def trace(self):
        summa = 0
        for i in range(self.n):
            summa += self.matrix[i][i]
        return summa
    def greater_than_average(self):
        l = [0 for _ in range(len(self.matrix))]
        average = 0
        for i in range(self.n):
            for j in range(self.m):
                average += self.matrix[i][j]
            average //= self.m
            for j in range(self.m):
                if(self.matrix[i][j] > average):
                    l[i] += 1
            average = 0
        return l
    def maximum_in_area_1(self):
        maximum = self.matrix[0][0]
        for i in range(self.n):
            for j in range(i + 1):
                if(maximum < self.matrix[i][j]):
                    maximum = self.matrix[i][j]
        return maximum
    def maximum_in_area_2(self):
        maximum = self.matrix[0][0]
        for i in range(self.n):
            for j in range(self.m):
                if(maximum < self.matrix[i][j] and ((i >= j and i <= self.n -1 - j) or (i <= j and i >= self.n -1 - j))):
                    maximum = self.matrix[i][j]
        return maximum
    def u_quarter(self):
        l = []
        for i in range(self.n):
            for j in range(self.m):
                if((i < j and i < self.n -1 - j)):
                    l.append(self.matrix[i][j])
        return l 
    def r_quarter(self):
        l = []
        for i in range(self.n):
            for j in range(self.m):
                if((i < j and i > self.n -1 - j)):
                    l.append(self.matrix[i][j])
        return l
    def d_quarter(self):
        l = []
        for i in range(self.n):
            for j in range(self.m):
                if((i > j and i > self.n -1 - j)):
                    l.append(self.matrix[i][j])
        return l
    def l_quarter(self):
        l = []
        for i in range(self.n):
            for j in range(self.m):
                if((i > j and i < self.n -1 - j)):
                    l.append(self.matrix[i][j])
        return l
    def multiplication_table(self):            
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] = i * j
    def maximum_in_the_table(self): 
        maximum = self.matrix[0][0]
        max_i, max_j = 0, 0
        for i in range(self.n):
            for j in range(self.m):
                if(maximum < self.matrix[i][j]):
                    maximum = self.matrix[i][j]
                    max_i, max_j = i, j
        return (max_i, max_j)
    def column_swapping(self, k = 0, l=0):
        new = self.transpose()
        new.matrix[k], new.matrix[l] = new.matrix[l], new.matrix[k]
        return new.transpose()
    def is_symmetric_matrix(self):
        flag = True
        for i in range(self.n):
            for j in range(i + 1):
                if(self.matrix[i][j] != self.matrix[j][i]):
                    flag = False
        return flag
    def diagonal_swapping(self):
        new = matrix()
        new.n = self.n
        new.m = self.m
        new.matrix = copy.deepcopy(self.matrix)
        for i in range(new.n):
            new.matrix[i][i], new.matrix[new.n - i - 1][i] = new.matrix[new.n - i - 1][i], new.matrix[i][i]
        return new
    def mirror_reflection(self): 
        new = matrix()
        new.n = self.n
        new.m = self.m
        new.matrix = copy.deepcopy(self.matrix)
        for i in range(new.n // 2):
            new.matrix[i], new.matrix[new.n - i - 1] = new.matrix[new.n - i - 1], new.matrix[i]
        return new
    def rotate_the_matrix(self):
        new = matrix()
        new.n = self.n
        new.m = self.m
        new.matrix = copy.deepcopy(self.matrix)
        for i in range(new.n):
            for j in range(new.m):
                new.matrix[j][i] = self.matrix[self.n - i - 1][j]
        return new
chess = matrix(8, 8, '.')
s = input()
x = ord(s[0]) - ord('a')
y = chess.n - int(s[1])
for i in range(chess.n):
    for j in range(chess.m):
        if((i - y)**2 + (j - x)**2 == 2 ** 2 + 1 ** 2):
            chess.matrix[i][j] = '*'
chess.matrix[y][x] = 'N'
chess.mprint()



st = input()
n, m = 8 - int(st[1]), ord(st[0]) - 97
[print(*['*' if (i - n) ** 2 + (j - m) ** 2 == 5 else 'N' if i == n and j == m else '.' for j in range(8)]) for i in range(8)]



# put your python code here
s = input()
dic = {'a' : 1,
        'b' : 2,
        'c' : 3,
        'd' : 4,
        'e' : 5,
        'f' : 6,
        'g' : 7,
        'h' : 8}

for i in range(8, 0, -1):
    for j in range(1, 8 + 1):
        if 2 == abs((dic[s[0]] - j) * (int(s[1]) - i)) :
            print('*', end=' ' )
        elif i == int(s[1]) and j == dic[s[0]]:
            print('N', end=' ')
        else:
            print('.', end= ' ' )


    print()



t, r = input(), range(8)
y, x = ord(t[0]) - ord("a"), int(t[1]) - 1
t = [[".*"[((x - i) ** 2 - (y - j) ** 2) ** 2 == 9] for j in r] for i in r]
t[x][y] = "N"

[print(*x) for x in t[::-1]]



f_ij = input()
f_i, f_j = '87654321'.index(f_ij[1]), ord(f_ij[0]) - 97
matrix = [['*' if (i - f_i)**2 + (j - f_j)**2 == 5 else '.' for j in range(8)] for i in range(8)]
matrix[f_i][f_j] = 'N'
[print(*row) for row in matrix]
'''