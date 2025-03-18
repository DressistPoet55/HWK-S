# Task 2 re
# 2
import re


with open('../dates.txt', 'w', encoding="utf-8") as file:
    file.write('11.03.2025 в 18:00 пойдёт дождь, а 12.03.2025 снег \n')

with open('../dates.txt', 'r', encoding="utf-8") as file:
    content = file.read()

dates = re.findall(r'\d{2}\.\d{2}\.\d{4}', content)

print('Даты:', dates)
print()

# 3
passwords = ['Pass123', '1234', 'abcd', 'ABCD', 'aB1']

for password in passwords:
    if len(password) >= 4 and re.search(r'[a-zA-Z]', password) and \
            re.search(r'\d', password):
        print(f'Пароль {password} верный')
    else:
        print(f'Неверный пароль {password}')
print()

# 4
sentence = ("Довольно распространённая ошибка ошибка — это лишний повтор повтор слова слова. "
            "Смешно, не не правда ли? Не нужно портить хор хоровод.")


pattern = re.compile(r'\b(\w+)(\s+\1\b)+', re.IGNORECASE)
corrected_sentence = pattern.sub(r'\1', sentence)

print("Исправленное предложение:", corrected_sentence)
