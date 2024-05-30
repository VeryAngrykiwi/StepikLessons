sea, vil, mou, sea_vil, vil_mou, DVI = [int(input()) for _ in range(6)]
sea_res = sea - sea_vil
vil_res = vil - vil_mou - sea_vil
mou_res = mou - vil_mou
student = sea_res + vil_res + mou_res + sea_vil + vil_mou + DVI
print(student)


'''
n, m, k, x, y, z = [int(input()) for _ in range(6)]

print(n + m + k - x - y + z)



print(int(input()) + int(input()) + int(input()) - int(input()) - int(input()) + int(input()))



n, m, k, x, y, z = (int(input()) for _ in range(6))
print(n + m - x + k - y + z)




# Считываем входящие числа.
n, m, k, x, y, z = (int(input()) for _ in range(6))

# Вычисляем результат.
result = (n - x) + x + (m - x - y) + y + (k - y) + z

# Выводим результат.
print(result)




print((lambda n, m, k, x, y, z: n + m + k - x - y + z)(*[int(input()) for _ in 'school']))
'''