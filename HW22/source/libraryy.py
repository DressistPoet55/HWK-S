# libraryy.py


class Book:
    def __init__(self, book_name, author, num_pages, isbn):
        self.book_name = book_name
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.reserv = None
        self.givenbook = None

    def reserve(self, reader):
        if self.reserv is None:
            self.reserv = reader
            return f'Книга {self.book_name} зарезервирована за {reader.name}'
        else:
            raise Exception("Книга уже заревервирована")

    def cancel_reserve(self, reader):
        if self.reserv == reader:
            self.reserv = None
            return f'Резервация на книгу {self.book_name} отменена'
        return 'Книга не зарезервирована за вами'

    def get_book(self, reader):
        if self.givenbook is None and self.reserv == reader:
            self.givenbook = reader
            self.reserv = None
            return f'Книга {self.book_name} выдана {reader.name}'
        elif self.givenbook is not None:
            return f'Книга {self.book_name} уже выдана другому пользователю'
        else:
            return 'Вы не можете взять книгу, так как она не зарезервирована'

    def return_book(self, reader):
        if self.givenbook == reader:
            self.givenbook = None
            return f'Книга {self.book_name} возвращена {reader.name}'
        else:
            return 'У вас нет книги'


class Reader:
    def __init__(self, name):
        self.name = name

    def reserve_book(self, book):
        return book.reserve(self)

    def cancel_reserve(self, book):
        return book.cancel_reserve(self)

    def get_book(self, book):
        return book.get_book(self)

    def return_book(self, book):
        return book.return_book(self)
