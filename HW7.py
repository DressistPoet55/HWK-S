# Task 1 Time

motomin1 = 240
motomin2 = 808
currenthours1 = motomin1 // 60
currenthours2 = motomin2 // 60
currentmin1 = motomin1 % 60
currentmin2 = motomin2 % 60
# print(f'{currenthours1:02d}:{currentmin1:02d}')
# print(f'{currenthours2:02d}:{currentmin2:02d}')

numbsum1 = (currenthours1 // 10) + (currenthours1 % 10) + (currentmin1 // 10) + (currentmin1 % 10)
numbsum2 = (currenthours2 // 10) + (currenthours2 % 10) + (currentmin2 // 10) + (currentmin2 % 10)

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

wrongtime = '00:00'
hh_str, mm_str = wrongtime.split(':')
hh = int(hh_str)
mm = int(mm_str)
daytime: str

if hh >= 12:
    if hh > 12:
        hh -= 12
    daytime = 'p.m.'
else:
    if hh == 0:
        hh = 12
    daytime = 'a.m.'

print(f"{hh}:{mm:02d} {daytime}")
