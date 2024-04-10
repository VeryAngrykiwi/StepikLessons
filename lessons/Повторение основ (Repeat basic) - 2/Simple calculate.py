import math

def sum (a,b) -> int:
  return a+b

def sub (a,b) -> int:
  return a-b

def mul (a,b) -> int:
  return a*b

def chastnoe (a,b) -> int:
  return a/b

def celoe (a,b) -> int:
  return a%b

def ostatok (a,b) -> int:
  return a//b

def stepen (a,b) -> int:
  a = a**10
  b = b**10
  return math.sqrt(a+b)  

def calculate():
  a = int(input())
  b = int(input())
  print(sum(a,b))
  print(sub(a,b))
  print(mul(a,b))
  print(chastnoe(a,b))
  print(ostatok(a,b))
  print(celoe(a,b))
  print(stepen(a,b))

calculate()
