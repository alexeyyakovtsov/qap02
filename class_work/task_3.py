my_str = input('Введиите номер билета: ')

part1 = my_str[:3]
part2 = my_str[3:]

for i in my_str:
    for j in part1:
        summa = 0
        summa += part1[j]
        print(summa)
