# Task Datetime
# 9
from datetime import datetime
#
#
# def calculate_date_difference(date1, date2):
#     date1 = datetime.strptime(date1, "%Y-%m-%d")
#     date2 = datetime.strptime(date2, "%Y-%m-%d")
#     days_difference = abs((date2 - date1).days)
#     return days_difference
#
#
# date11 = input('Первая дата (ГГГГ-ММ-ДД): ')
# date22 = input('Вторая дата (ГГГГ-ММ-ДД): ')
# days_diff = calculate_date_difference(date11, date22)
# print(f"Количество дней между двумя датами: {days_diff}")


# 10
def check_date(input_date):
    kog_date = datetime.strptime(kog_date_in, "%Y-%m-%d")
    current_date = datetime.now()
    if kog_date > current_date:
        return 'Введенная дата находится в будущем'
    elif kog_date < current_date:
        return 'Введенная дата находится в прошлом'
    else:
        return 'Вы ввели текущую дату'


kog_date_in = input("Введите дату (ГГГГ-ММ-ДД): ")
result = check_date(kog_date_in)
print(result)
