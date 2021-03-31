def bank_vklad(a):
    def vklad_years(years):
        sum_vklad = 0
        for i in range(years):
            procent_vklad = (a * 10) / 100
            sum_vklad += a + procent_vklad
            return sum_vklad

    return vklad_years

new_vklad = bank_vklad(int(input('Введите сумму: ')))
print(new_vklad(10))