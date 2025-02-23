# Task 1 Последовательность
def solution(sequence):
    count = 0
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            count += 1
            if count > 1:
                return False
            if (i > 0 and sequence[i - 1] >= sequence[i + 1]
                    and (i + 2 < len(sequence) and sequence[i] >= sequence[i + 2])):
                return False
    return True


print(solution([1, 2, 3]))
print(solution([1, 2, 1, 2]))
print(solution([1, 3, 2, 1]))
print(solution([1, 2, 3, 4, 5, 3, 5, 6]))
print(solution([40, 50, 60, 10, 20, 30]))


# Task 2 Число напротив
def opposite(n, f_number):
    return (f_number + n // 2) % n


print(opposite(10, 6))
print(opposite(10, 2))
print(opposite(10, 4))


# Task 3 Validate
def valid(card):
    numb = str(card)
    if not numb.isdigit() or len(numb) == 0 or len(str(numb)) < 13 or len(str(numb)) > 19:
        return "Неверная карта"
    total_sum = 0
    length = len(numb)
    for i in range(length):
        digit = int(numb[length - 1 - i])
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total_sum += digit
    return total_sum % 10 == 0


print(valid(4561261212345464))
print(valid(4561261212345467))
print(valid(4222222222222))
print(valid(5555555555554444))
