
number = [int(i) for i in input().split()]
counter = 0
for x in range(len(number)):
  if number[x] > number[x-1]:
    counter += 1

print (counter)

'''
numbers = list(map(int, input().split()))
count = sum([1 for i in range(1, len(numbers)) if numbers[i] > numbers[i - 1]])
print(count)

nums = tuple(map(int, input().split()))
print(sum(1 for i in range(1, len(nums)) if nums[i-1] < nums[i]))

a = tuple(map(int, input().split()))
print(sum(a[i - 1] < a[i] for i in range(1, len(a))))

print(sum([l[i] > l[i - 1] for l in [list(map(int, input().split()))] for i in range(1, len(l))]))

s = list(map(int, input().split()))
c = 0
for i in range(len(s) - 1):
    if s[i] < s[i + 1]:
        c += 1
print(c)

s = [int(n) for n in input().split()]
counter = 0
previous = s[0]
for i in range(len(s)):
  if s[i] > previous:
    counter += 1
  previous = s[i]
print(counter)

print((lambda n: sum([x < n[i+1] for i, x in enumerate(n[:-1])]))(list(map(int, input().split()))))
'''
