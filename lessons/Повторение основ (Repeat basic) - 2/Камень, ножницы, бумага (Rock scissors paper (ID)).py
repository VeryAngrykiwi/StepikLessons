Timur = input()
Ruslan = input()

if Timur == Ruslan:
  print('ничья')
elif Timur == 'камень' and Ruslan == 'ножницы':
  print('Тимур')
elif Timur == 'ножницы' and Ruslan == 'бумага':
  print('Тимур')
elif Timur == 'бумага' and Ruslan == 'камень':
  print('Тимур')
else:
  print('Руслан')

'''
options = ["камень", "ножницы", "бумага"]
results = ["ничья", "Руслан", "Тимур"]

timur_move = input()
ruslan_move = input()

case = options.index(timur_move) - options.index(ruslan_move)
res = results[case]

print(res)


x, y = input(), input()
var = ['камень', 'ножницы', 'бумага']
ans = ['ничья', 'Руслан', 'Тимур']
print(ans[var.index(x) - var.index(y)])


print(['ничья', 'Тимур', 'Руслан'][input().count('а') - input().count('а')])


a, b = input(), input()
print('ничья' if a == b else 'Тимур' if a + b in ('каменьножницы', 'бумагакамень', 'ножницыбумага') else 'Руслан')

tim_rus = input() + ' ' + input()

def game(tim_rus):

    draw = ['камень камень', 'бумага бумага', 'ножницы ножницы']
    lose = ['ножницы камень', 'камень бумага', 'бумага ножницы']
    win = ['камень ножницы', 'бумага камень', 'ножницы бумага']

    if tim_rus in draw:
        return 'ничья'
    if tim_rus in lose:
        return 'Руслан'
    if tim_rus in win:
        return 'Тимур'
    else:
        return 'слыш ты че, нормально делай'


print(game(tim_rus))
'''
