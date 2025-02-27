# Task 1 Быки и коровы
# Загадано число 3219
import random

number = random.sample(range(0, 4), 4)
while number:
    bull = 0
    cow = 0
    answr = input('Введите число:')
    if len(answr) != 4 or answr.isalpha():
        print('Ошибка: введи 4-значное число')
    for i in range(4):
        if int(answr[i]) == number[i]:
            bull += 1
        elif int(answr[i]) in number:
            cow += 1
    print(f"{bull} быков, {cow} коров")
    if bull == 4:
        print('Вы отгадал число!')
        break


# Task 2 Пирамида
N = 10
n = 1
while n <= N:
    sp = N - n
    st = 2 * n - 1
    i = 0
    while i < sp:
        print(' ', end='')
        i += 1
    x = 0
    while x < st:
        print('*', end='')
        x += 1
    print()
    n += 1


# Task 3 Статуи
statues = [6, 2, 3, 8]
min_size = min(statues)
max_size = max(statues)
misstat = 0
current_size = min_size
while current_size <= max_size:
    count = 0
    for size in statues:
        if size == current_size:
            count += 1
    if count == 0:
        misstat += 1
    current_size += 1

print(misstat)
