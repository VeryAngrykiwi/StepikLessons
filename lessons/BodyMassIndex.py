def BMI(height, weight) -> float:
  BMI = weight / (height ** 2)
  if BMI >= 18.5 and BMI <=25:
    return "Оптимальная масса"
  elif BMI < 18.5:
    return "Недостаточная масса"
  else:
    return "Избыточная масса"

def main():
  weight = float(input())
  height = float(input())
  print(BMI(height, weight))

main()