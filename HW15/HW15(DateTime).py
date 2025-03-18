# Task Datetime
# 9
from datetime import datetime
from dateutil.relativedelta import relativedelta


date1_in = input('Первая дата (ГГГГ-ММ-ДД): ')
date2_in = input('Вторая дата (ГГГГ-ММ-ДД): ')

date1 = datetime.strptime(date1_in, "%Y-%m-%d")
date2 = datetime.strptime(date2_in, "%Y-%m-%d")

difference = relativedelta(date2, date1)

days_difference = abs((date2 - date1).days)
print(f"Количество дней между двумя датами: {days_difference}")


# 10
kog_date_in = input("Введите дату (ГГГГ-ММ-ДД): ")
kog_date = datetime.strptime(kog_date_in, "%Y-%m-%d")
current_date = datetime.now()

if kog_date > current_date:
    print('Введенная дата находится в будущем')
elif kog_date < current_date:
    print('Введенная дата находится в прошлом')
else:
    print('Вы ввели текущую дату')
