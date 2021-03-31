def reverse(number):
    return number[::-1]

def other_reverse(number):
    s = list(reversed(number))
    return s

b = reverse(input('Введите число '))
st = other_reverse(input('Введиет число 2: '))
print(b)
print(st, sep='')
