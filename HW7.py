# Task 1 Time

motomin1 = 240
motomin2 = 808
currenthours1 = 240 // 60
currenthours2 = 808 // 60
currentmin1 = 240 % 60
currentmin2 = 808 % 60
# print(f'{currenthours1:02d}:{currentmin1:02d}')
# print(f'{currenthours2:02d}:{currentmin2:02d}')

numb1hour1 = currenthours1 // 10
numb1hour2 = currenthours1 % 10
numb1min1 = currentmin1 // 10
numb1min2 = currentmin1 % 10

numb2hour1 = currenthours2 // 10
numb2hour2 = currenthours2 % 10
numb2min1 = currentmin2 // 10
numb2min2 = currentmin2 % 10

numbsum1 = numb1hour1 + numb1hour2 + numb1min1 + numb1min2
numbsum2 = numb2hour1 + numb2hour2 + numb2min1 + numb2min2
print(numbsum1)
print(numbsum2)


# Task 2 Level Up

experience = 10
reward = 5
# threshold = experience + reward
threshold = 15
if experience + reward >= 15:
    print('Congrats!(True)')
elif experience + reward < 15:
    print('Weak!(False)')


# Task 3 Time converter

wrongtime = '12:30'
hh,mm = wrongtime.split(':')
hh = int(hh)
mm = int(mm)
if hh >= 12:
    if hh > 12:
        hh -= 12
    if hh == 12:
        hh = 12
    daytime = 'p.m.'
    print(f"{hh}:{mm:02d} {daytime}")
elif hh < 12:
    if hh == 0:
        hh = 12
    daytime = 'a.m.'
    print(f"{hh}:{mm:02d} {daytime}")
