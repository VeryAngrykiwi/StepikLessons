print(len(input().split()))

'''
text = input()
word = 0
count = 0
for letter in text:
    if letter != " ": 
        count += 1
    elif count > 0:
        word += 1
        count = 0
if count > 0:
    word += 1
print(word)

s = input()
count = 1
for i in range(len(s)):
    if s[i] == ' ' and s[i+1] != ' ':
        count+= 1
print(count)

str_calc_num_of_words = input()
num_words = 0
flag = 0
for i in range(len(str_calc_num_of_words)):
    if str_calc_num_of_words[i] not in ' .,!?:;' and flag == 0:
        num_words += 1
        flag = 1
    else:
        if str_calc_num_of_words[i] == ' ':
            flag = 0
print(num_words)

def countWords (str): return print(len(str.split())); 
str = "Freedom Антохе-Криминалу, без него не кому голы забивать!"; countWords(str)

countWords2 = lambda str: print(len(str.split()));countWords2("Timur forever young")


count_words = lambda s: sum(1 for _ in s.split())
'''
