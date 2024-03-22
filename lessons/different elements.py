s = input().split()
s2 = []
for i in s:
  if i not in s2:
      s2.append(i)
print(len(s2))



'''
numbers = input().split()
counter = 1

for i in range(len(numbers) - 1):
    if numbers[i] != numbers[i + 1]:
        counter += 1

print(counter)

# Read input from the user
input_str = input()

# Convert input string to list of integers
numbers_list = list(map(int, input_str.split()))

# Count number of unique elements in the list
count_unique_elements = len(set(numbers_list))

# Output the count of different elements
print(count_unique_elements)

print(len(set(input().split())))

a = input().split()
print(len([i for i in range(len(a)) if a[i] not in a[:i]]))

numbers = input() + ' '
counter = 0

space = numbers.find(' ')
number = int(numbers[:space])
num = str(number - 1)

while len(numbers) != 0:
    space = numbers.find(' ')
    number = numbers[:space]
    if number != num:
        counter += 1
        num = number
    numbers = numbers[space + 1:]

print(counter)

print((lambda n: sum([x != n[i+1] for i, x in enumerate(n[:-1])])+1)(input().split()))

ls =  list(map(int, input().split()))
print(sum(map(lambda x: x[1]>x[0], zip(ls[:-1], ls[1:]))) + 1)
'''