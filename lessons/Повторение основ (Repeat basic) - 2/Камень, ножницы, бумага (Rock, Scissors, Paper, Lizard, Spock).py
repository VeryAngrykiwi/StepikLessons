Timur = input()
Ruslan = input()

if Timur == Ruslan:
  print('ничья')
elif Timur == 'камень' and (Ruslan == 'ножницы' or Ruslan == 'ящерица'):
  print('Тимур')
elif Timur == 'ножницы' and (Ruslan == 'бумага' or Ruslan == 'ящерица'):
  print('Тимур')
elif Timur == 'бумага' and (Ruslan == 'камень' or Ruslan == 'Спок'):
  print('Тимур')
elif Timur == 'ящерица' and (Ruslan == 'бумага' or Ruslan == 'Спок'):
  print ('Тимур')
elif Timur == 'Спок' and (Ruslan == 'камень' or Ruslan == 'ножницы'):
  print ('Тимур')
else:
  print('Руслан')

'''
options = ["rock", "scissors", "paper", "lizard", "spock"]
results = ["draw", "Timur", "Ruslan"]

Timur = input()
Ruslan = input()

if Timur == Ruslan:
    print('draw')
elif Timur == 'rock' and Ruslan == 'scissors':
    print('Timur')
elif Timur == 'scissors' and Ruslan == 'paper':
    print('Timur')
elif Timur == 'paper' and Ruslan == 'rock':
    print('Timur')
elif Timur == 'rock' and Ruslan == 'lizard':
    print('Timur')
elif Timur == 'lizard' and Ruslan == 'spock':
    print('Timur')
elif Timur == 'spock' and Ruslan == 'scissors':
    print('Timur')
elif Timur == 'scissors' and Ruslan == 'lizard':
    print('Timur')
elif Timur == 'lizard' and Ruslan == 'paper':
    print('Timur')
elif Timur == 'paper' and Ruslan == 'spock':
    print('Timur')
elif Timur == 'spock' and Ruslan == 'rock':
    print('Timur')
else:
    print('Ruslan')


options = ["камень", "ящерица", "Спок", "ножницы", "бумага"]
results = ["ничья", "Руслан", "Тимур", "Руслан", "Тимур"]

timur_move = input()
ruslan_move = input()

case = options.index(timur_move) - options.index(ruslan_move)
res = results[case]

g = ('ножницы', 'бумага', 'камень', 'ящерица', 'Спок')
dist = (g.index(input()) - g.index(input())) % len(g)
print(('ничья', 'Тимур', 'Руслан')[dist and dist % 2 + 1])


a, b = input()[0], input()[0]
print('ничья' if a == b else 'Тимур' if a + b in ('кн', 'бк', 'нб', 'кя', 'яС', 'Сн', 'ня', 'яб', 'бС', 'Ск') else 'Руслан')


a = 'ножницыбумагакаменьящерицаСпокножницыящерицабумагаСпоккаменьножницы'
t, r = input(), input()
if t == r:
  print('ничья')
elif t + r in a:
  print('Тимур')
else:
  print('Руслан')


s = ["ножницы", "бумага", "камень", "ящерица", "Спок", "ножницы", "бумага", "камень", "ящерица", "Спок"]
s1, s2 = input(), input()
if s1 == s2:
    print("ничья")
elif s2 == s[s.index(s1) - 2] or s2 == s[s.index(s1) + 1]:
    print("Тимур")
else:
    print("Руслан")


timur, ruslan = input(), input()
winner = 'Тимур'

if timur == ruslan:
    winner = 'ничья'
elif (
      timur == 'камень' and ruslan in ('бумага', 'Спок') or 
      timur == 'ножницы' and ruslan in ('камень', 'Спок') or 
      timur == 'бумага' and ruslan in ('ножницы', 'ящерица') or
      timur == 'ящерица' and ruslan in ('камень', 'ножницы') or
      timur == 'Спок' and ruslan in ('бумага', 'ящерица')
     ):
    winner = 'Руслан'
    
print(winner) 
'''
