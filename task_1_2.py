x = int(input('Vvedite x: '))
y = int(input('Vvedite y: '))

z = (abs(x) - abs(y)) / (1 + abs(x * y))

print(str(z))