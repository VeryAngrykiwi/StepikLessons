def func(num1, num2):
  return num1 % num2 == 0

num1, num2 = int(input()), int(input())

if func(num1, num2):
    print('делится')
else:
  print('не делится')

'''
def func(num1, num2):
    return not num1 % num2


print(f"{'не ' * (not func(int(input()), int(input())))}делится")

print(['делится', 'не делится'][bool(float(input()) % float(input()))])
'''