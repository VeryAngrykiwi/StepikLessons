def lineCost(str):
  cost = len(str) * 0.60
  rub = int(cost)
  kop = round((cost - rub) * 100)
  return f"{rub} руб. {kop} коп."

def main():
  str = input()
  print(lineCost(str))

main()

'''
string = input()
price = 60 * len(string)

print(f'{price // 100} р. {price % 100} коп.')
'''
