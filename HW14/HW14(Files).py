# Task 1 Files
# 1
def write_students_to_file(filename):
    with open('../students.txt', 'w', encoding="utf-8") as file:
        file.write('Var, Group1, 9, 3, 1\n')
        file.write('Pal, Group1, 5, 6, 7\n')
        file.write('Lok, Group2, 5, 8, 8\n')
        file.write('Mage, Group2, 9, 9, 8\n')


def process_student_line(line):
    parts = line.strip().split(', ')
    name = parts[0]
    groups = parts[1]
    grades = list(map(int, parts[2:]))
    return {'name': name, 'group': groups, 'grades': grades}


def read_students_from_file(filename):
    with open(filename, 'r', encoding="utf-8") as files:
        return [process_student_line(line) for line in files]


def get_students(filename):
    return read_students_from_file(filename)

students = get_students('../students.txt')

total_students = len(students)
group_info = {}

for student in students:
    group = student['group']
    if group not in group_info:
        group_info[group] = {'count': 0, 'total_grades': 0}

    group_info[group]['count'] += 1
    group_info[group]['total_grades'] += sum(student['grades'])

print(f"\nОбщее количество студентов: {total_students}")
for group, info in group_info.items():
    avg_grade = info['total_grades'] / (info['count'] * 3)
    print(f"Группа {group}: {info['count']} студентов, Средняя оценка: {avg_grade:.2f}")
