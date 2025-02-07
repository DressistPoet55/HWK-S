# Task 1
# Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'

q1 = "www.my_site.com#about"
print(q1.replace("#", "/"))


# Task 2
# Напишите программу, которая добавляет ‘ing’ к словам

word = "Слово"
print(f"{word}ing")


# Task 3
# В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"

name_surname = 'Ivanou Ivan'
detached = name_surname.split()
correct = detached[::-1]
print(" ".join(correct))


# Task 4
# Напишите программу, которая удаляет пробел в начале, в конце строки

probel = ' levopravo '

print(probel.lstrip())
print(probel.rstrip())


# Task 5
# Имена собственные всегда начинаются с заглавной буквы, за которой следуют строчные буквы.
# Исправьте данное имя собственное так, чтобы оно соответствовало этому утверждению.
# "pARiS" >> "Paris"

task5 = "pARiS"
print(task5.capitalize())


# Task 6
# Перевести строку в список
# "Robin Singh" => ["Robin”, “Singh"]

task6 = "Robin Singh"
print(task6.split())


# Task 7
#   "I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"]

tsk7 = 'I love arrays they are my favorite'
print(tsk7.split())


# Task 8
# Дан список: [Ivan, Ivanou], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”

Line = ['Ivan', 'Ivanou']
strokone = " ".join(Line)
stroktwo = 'Minsk, Belarus'
print(f"Привет, {strokone} ! Добро пожаловать в {stroktwo} ")


# Task 9
# Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"]
# сделайте из него строку => "I love arrays they are my favorite"

spisok = ["I", "love", "arrays", "they", "are", "my", "favorite"]
print("".join(spisok))

# Task 10
# Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
# удалите элемент из списка под индексом 6

bigspisok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newnumber = 333
bigspisok.insert(2, newnumber)
del bigspisok[6]
print(bigspisok)
