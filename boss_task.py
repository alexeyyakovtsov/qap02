#events, liters  = input('Введите действие: '), int(input('Введите литры: '))


MAX_B1 = 5
MAX_B2 = 3

b1 = b2 = 0

while True:
    b1 = MAX_B1 #5

    b1 = b1 - (MAX_B2 - b2) #2
    b2 = MAX_B1 - b1 #3
    print('b1 = ' + str(b1))
    print('b2 = ' + str(b2))

    if (b1 == 4):
        break

    b2 = 0 

    b2 = b1 - b2 #2
    print(b2)
    b1 = b1 - b1 #0
    print(b1)
