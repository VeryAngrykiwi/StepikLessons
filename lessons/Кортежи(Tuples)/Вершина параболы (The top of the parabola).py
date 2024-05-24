a,b,c = [int(input()) for _ in range(3)]
x = -b/(a*2)
y = (4 * a * c - b ** 2) / (4 * a)
print((x, y))

'''
a, b, c = (int(input()) for _ in range(3))
print((-b / 2 / a, (4 * a * c - b * b) / 4 / a))



a, b, c = int(input()),  int(input()),  int(input())
print(tuple([-b / (2 * a), (4 * a *c - b * b) / (4 * a)]))



(lambda a, b, c: print(tuple([-b/(2*a), (4*a*c-b**2)/(4*a)])))(*[int(input()) for _ in 'abc'])



# put your python code here
class Discrim:
  def __init__(self, a, b, c):
    print(self.__alg__(a, b, c))

  def __alg__(self, a, b, c):
    x1 = -b / (2 * a)
    x2 = (4 * a * c - b ** 2) / (4 * a)
    return x1, x2

if __name__ == '__main__':
  Discrim(*[int(input()) for _ in range(3)])



from math import pow
t = []
a, b, c = int(input()), int(input()), int(input())
x1 = -(b/(2*a))
y1 = ((4*a*c - pow(b, 2))/(4*a))

t.append(x1)
t.append(y1)

print(tuple(t))
'''