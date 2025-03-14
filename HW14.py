import re
import xml.etree.ElementTree as ET
import json
import yaml


# Task 1 Files
# 1
with open('students.txt', 'w', encoding="utf-8") as file:
    file.write('Var, Group1, 9, 3, 1\n')
    file.write('Pal, Group1, 5, 6, 7\n')
    file.write('Lok, Group2, 5, 8, 8\n')
    file.write('Mage, Group2, 9, 9, 8\n')

with open('students.txt', 'r', encoding="utf-8") as file:
    for line in file:
        print(line, end='')

students = []
with open('students.txt', 'r', encoding="utf-8") as file:
    for line in file:
        parts = line.strip().split(', ')
        name, group = parts[0], parts[1]
        grades = parts[2:]
        grades = list(map(str, grades))
        students.append({'name': name, 'group': group, 'grades': grades})

total_students = len(students)
group_info = {}

for student in students:
    group = student['group']
    if group not in group_info:
        group_info[group] = {'count': 0, 'total_grades': 0, 'total_students': 0}

    group_info[group]['count'] += 1
    group_info[group]['total_grades'] += sum(map(int, student['grades']))
    group_info[group]['total_students'] += len(student['grades'])

print(f"\nОбщее количество студентов: {total_students}")
for group, info in group_info.items():
    avg_grade = info['total_grades'] / info['total_students']
    print(f"Группа {group}: {info['count']} студентов, Средняя оценка: {avg_grade:.2f}")
print()

# Task 2 re
# 2


with open('dates.txt', 'w', encoding="utf-8") as file:
    file.write('11.03.2025 в 18:00 пойдёт дождь, а 12.03.2025 снег \n')

with open('dates.txt', 'r', encoding="utf-8") as file:
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
print()


# Task 3 XML
# 5


def parsexml(xml_str):
    root = ET.fromstring(xml_str)
    total_cost = 0

    for child in root:
        print(child.tag, child.attrib)
        print(child[0].text)

    for product in root.findall('product'):
        price = float(product.find('price').text)
        koll = int(product.find('koll').text)
        total_cost += price * koll
        print(f"{price} => {koll}")

    return total_cost


if __name__ == "__main__":
    xml_string = """<?xml version="1.0" encoding="UTF-8"?>
        <products>
            <product name='Product1'>
               <price>22</price>
               <koll>1</koll>
            </product>
            <product name='Product2'>
               <price>33</price>
               <koll>2</koll>
            </product>
        </products>
        """
    total_cost1 = parsexml(xml_string)
    print(f"Общая стоимость всех товаров: {total_cost1}")
print()

# Task 4
# 6


fk1 = {
    'name': 'Bavaria',
    'country': 'Germany',
    'wins': 33
}
fk2 = {
    'name': 'Legia',
    'country': 'Poland',
    'wins': 22
}
fk3 = {
    'name': 'Leh',
    'country': 'Poland',
    'wins': 11
}

fks = [fk1, fk2, fk3]

json_data = json.dumps(fks)


def get_wins(club):
    return club['wins']


max_wins_fk = max(fks, key=get_wins)

print(json_data)
print(f"Клуб с наибольшим количеством побед:{max_wins_fk}")
print()

# Task 5 YAML
# 7


books = """
- title: 'The Lord of the Rings'
  author: 'J. R. R. Tolkien'
  year: 1954
- title: 'The Hobbit'
  author: 'J. R. R. Tolkien'
  year: 1937
- title: 'The Lord of the Rings: The Return of the King'
  author: 'J. R. R. Tolkien'
  year: 1955
"""
to_yaml = yaml.safe_load(books)

with open('books.yaml', 'w', encoding="utf-8") as library:
    yaml.dump(to_yaml, library)


def add_book(file_name, title, author, year):
    with open(file_name, 'r', encoding="utf-8") as file1:
        data = yaml.safe_load(file1)
    new_book = {'title': title, 'author': author, 'year': year}
    data.append(new_book)
    with open(file_name, 'w', encoding="utf-8") as file1:
        yaml.safe_dump(data, file1)


file_name1 = 'books.yaml'

add_book(file_name1, "The Lord of the Rings: The Two Towers", "J. R. R. Tolkien", 1954)

with open('books.yaml', 'r', encoding="utf-8") as f:
    templates = yaml.safe_load(f)

print(templates)
