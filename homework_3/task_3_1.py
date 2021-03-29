from prettytable import PrettyTable


try:
    aa = int(input('Введите число a: '))
    bb = int(input('Введите число b: '))
    cc = int(input('Введите число c: '))
    dd = int(input('Введите число d: '))

    x = PrettyTable()
    x.field_names = ['Activity', 'Result', 'Activity2', 'Result2', 
                    'Activity3', 'Result3', 'Activity4', 'Result4']

    if aa > 0 and bb > 0 and cc > 0 and dd > 0:
        for i in range(11):
            x.add_row([f'{aa} * {i} =', aa * i, f'{bb} * {i} =', bb * i, 
                        f'{cc} * {i} =', cc * i, f'{dd} * {i} =', dd * i])
            #x.add_row([f'{bb} * {i} =', bb * i])
            #x.add_row([f'{cc} * {i} =', cc * i])
            #x.add_row([f'{dd} * {i} =', dd * i])
        print(x)
    else:
        print('Введеное значение отрицательно')

except ValueError:
    print('Ошибка - введено не число')
