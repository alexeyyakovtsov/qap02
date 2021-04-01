from datetime import datetime

start_time = datetime.now()

def collac(number):
    while number != 1:
        print(number)
        if number % 2 == 0:
            number = number / 2
        elif number % 2 == 1:
            number = number * 3 + 1
        
    print(number)

a = collac(int(input('Введите число: ')))
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
