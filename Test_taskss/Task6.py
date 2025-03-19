# Task 6
def write_to_file(filename1):
    with open(filename1, 'w', encoding="utf-8") as file:
        file.write('abcde\n')


def read_file(filename1):
    with open(filename1, 'r', encoding='utf-8') as file:
        content = file.readlines()
        return content


def info(lines):
    num_lines = len(lines)
    num_words = sum(len(line.split()) for line in lines)
    num_simv = sum(len(line) for line in lines)
    return num_lines, num_words, num_simv


def info_aboutfile(filename1):
    lines = read_file(filename1)
    num_lines, num_words, num_simv = info(lines)
    inf = f'Cтроки:{num_lines}, слова:{num_words}, символы:{num_simv}'
    print(inf)
    with open(filename1, 'a', encoding='utf-8') as file:
        file.write(inf)


filename = 'example.txt'
write_to_file(filename)
read_file(filename)
info_aboutfile(filename)
read_file(filename)
