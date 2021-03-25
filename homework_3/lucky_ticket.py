ticket = input('Введите номер билета: ')

part1 = ticket[:3]
part2 = ticket[3:]
result = []

for index in (part1, part2):
    summ = 0
    for val in index:
        summ += int(val)
    result.append(summ)
    print(result)

"""    if result[0] == result[1]:
        print('Lucky')
    else:
        print('Usual')"""
