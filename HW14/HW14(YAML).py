# Task 5 YAML
# 7
import yaml


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

with open('../books.yaml', 'w', encoding="utf-8") as library:
    yaml.dump(to_yaml, library)


def add_book(file_name, title, author, year):
    with open(file_name, 'r', encoding="utf-8") as file1:
        data = yaml.safe_load(file1)
    new_book = {'title': title, 'author': author, 'year': year}
    data.append(new_book)
    with open(file_name, 'w', encoding="utf-8") as file1:
        yaml.safe_dump(data, file1)


file_name1 = '../books.yaml'

add_book(file_name1, "The Lord of the Rings: The Two Towers", "J. R. R. Tolkien", 1954)

with open('../books.yaml', 'r', encoding="utf-8") as f:
    templates = yaml.safe_load(f)

print(templates)
