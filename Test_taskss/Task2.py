# Task 2
def kvard_chisla():
    chislo = int(input('Введите число: '))
    kvadr = chislo ** 2
    print(kvadr)


def chet_or_not():
    chislo2 = int(input('Введите число: '))
    if chislo2 % 2 == 0:
        print('Число четное')
    else:
        print('Число нечетное')


kvard_chisla()
chet_or_not()
