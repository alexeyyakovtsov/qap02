MAX_B5 = 5
MAX_B3 = 3

bucket_5 = bucket_3 = 0

while bucket_5 != 4:
    print(f'Ведро 5л = {bucket_5}, Ведро 3л = {bucket_3}\n')

    change = input(f'Выберете ведро 3 или 5: ')
    print(f'Выбрано {change} ведро')
    event = input('Выберете действие: ')

    if change == '5':
        if event == 'fill':
            bucket_5 = 5
            print('Ведро 5 наполнено  \n')
        
        elif event == 'clear':
            bucket_5 = 0
        
        elif event == 'move':
            if bucket_5 == 2:
                bucket_3 = bucket_5
                bucket_5 = 0
            else:    
                bucket_5 = bucket_5 - (MAX_B3 - bucket_3)
                bucket_3 = MAX_B5 - bucket_5
        
    if change == '3':
        if event == 'fill':
            bucket_3 = 3
            print('Ведро 3 наполнено \n')
        
        elif event == 'clear':
            bucket_3 = 0

        elif event == 'move':
            bucket_5 = bucket_3
            bucket_3 = 0
else:
    print('Вы великолепны!!!')
