import time

def collac(number):
    for i in range(1_000_000):
        summa = 0
        if number % 2 == 0:
            summa = number / 2
        elif number % 2 == 1:
            summa = number * 3 + 1
        
        return f'{number} -> {summa}'

a = collac(int(input('Введите число: ')))
print(a)