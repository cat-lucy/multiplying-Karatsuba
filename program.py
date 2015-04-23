from Karatsuba_Multiply import *
while True:
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    ans = Karatsuba_Multiply().multiply(a, b)
    print (ans)
