from prettytable import PrettyTable


try:
    aa = int(input('Введите число a: '))
    bb = int(input('Введите число b: '))
    cc = int(input('Введите число c: '))
    dd = int(input('Введите число d: '))

    x = PrettyTable()
    x.field_names = ['Activity', 'Result']

    if aa > 0 and bb > 0 and cc > 0 and dd > 0:
        for i in range(11):
            x.add_row([f'{aa} * {i} =', aa * i])
        print(x)
    else:
        print('Введеное значение отрицательно')

except ValueError:
    print('Ошибка - введено не число')
