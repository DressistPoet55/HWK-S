# Task 4
def add_one(spis):
    one = 1
    new_spis = []
    for i in reversed(spis):
        new_digit = i + one
        if new_digit == 10:
            new_spis.append(0)
            one = 1
        else:
            new_spis.append(new_digit)
            one = 0
    if one == 1:
        new_spis.append(1)
    new_spis.reverse()
    return new_spis


print(add_one([9]))
print(add_one([1, 2, 3]))
print(add_one([1, 1, 9]))
print(add_one([9, 9, 9]))
