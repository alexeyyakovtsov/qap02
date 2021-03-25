from prettytable import PrettyTable

try:
    number = int(input('Введите цифру из таблицы умножения: '))
    x = PrettyTable()
    x.field_names = ['Activity', 'Result']
    for i in range(11):
        x.add_row([f'{number} * {i} =', number * i])
    print(x)

except ValueError:
    print('Ошибка - введено не число')

