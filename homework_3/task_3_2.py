count_prog = int(input('Введите число студентов: '))

l1 = ['программистов', 'программист', 'программиста']

try:
    if count_prog >= 0:
        if count_prog == 0:
            print(f'{count_prog} {l1[0]}')
        elif count_prog == 1:
            print(f'{count_prog} {l1[1]}')
        elif count_prog % 10 >=2 and count_prog % 10 <= 4:
            print(f'{count_prog} {l1[2]}')
        elif count_prog % 100 >= 10 and count_prog % 100 <= 20:
            print(f'{count_prog} {l1[0]}')
        else:
            print(f'{count_prog} {l1[0]}')

except ValueError:
    print('Введенное значение не является числом')