num = int(input('Введите число гостей: '))

if num >= 50:
    print('Ресторан')
elif 20 <= num < 50:
    print('Кафе')
elif num < 20:
    print('Дом')
else:
    print('Что-то пошло не так')