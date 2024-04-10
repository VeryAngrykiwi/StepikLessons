num = input('Введите число:')
print(int(num[:-5] + num[-5:][::-1]))

'''
num = input()
if len(num) == 5:
    print(int(num[-1::-1]))
else:
    print(int(num[0] + num[-1:-6:-1]))

a = input()
d = 0
b = str()
c = str()
if len(a) == 6:
    b = a[:0:-1]
    c = a[0] + b
    d = int(c)
    print(d)
if len(a) == 5:
    b = a[::-1]
    if b[-1] != 0:
        d = int(b)
        print(d)
    else:
        for i in range(len(a)):
            if b[i] != '0':
                c += b[i]
        d = int(c)
    print(c)

(lambda x: print(int(x[:-5] + x[-5:][::-1])))(input())

def IntRev(num):
    if len(num) == 5:
        return int(num[-1::-1])
    else:
        return int(num[0] + num[-1:-6:-1])

print(IntRev(input('Введите число: ')))
'''
