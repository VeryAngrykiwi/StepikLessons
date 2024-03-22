x = input().split()
print(*[x[-1]] + x[:len(x) - 1])



'''
seq = input().split()
new_seq = [seq[-1]] + seq[:-1]

print(*new_seq)

a = input().split()

print(*[a[-1]] + a[:-1])

n=input().split()
print(n.pop(), *n)

[print(l[-1], *l[:-1]) for l in [input().split()]]

def shift_list_elements(input_str):
  # Convert input string to a list of integers
  elements = list(map(int, input_str.split()))

  # Shift elements to the right
  shifted_elements = [elements[-1]] + elements[:-1]

  return shifted_elements

# Input
input_str = input()
result = shift_list_elements(input_str)

# Output
print(*result)

for i in range(1,len(a)):
    a[0],a[i] = a[i], a[0]
print(' '.join(a))

s = list(map(int, input().split()))
n = []
n.append(s[-1])
n.extend(s[:-1])
print(*n)

(lambda x: print(x.pop(), *x))(input().split())

print(*[f'{x.pop()} {" ".join(x)}' for x in [list(map(str, input().split()))]])

print(*[(l := input().split())[-1]] + l[:-1])
'''