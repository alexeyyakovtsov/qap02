def dna_fnc(a):
    l = len(a)
    count = 1

    for i in range(l):
        if i == (l -1):
            print(a[i] + str(count), end='')
        else:
            if a[i] == a[i +1]:
                count += 1
            else:
                print(a[i] + str(count), end='')
                count = 1


dna = dna_fnc(input('Введите строку ДНК: '))