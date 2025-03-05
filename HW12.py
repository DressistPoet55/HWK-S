# Task 1 Банковский вклад
class Deposit:
    def __init__(self, start_balance, years, interest_rate=0.10):
        self.start_balance = start_balance
        self.years = years
        self.interest_rate = interest_rate
        self.koll_months = years * 12


    def calculate_final_amount(self):
        monthly_rate = self.interest_rate / 12
        final_amount = self.start_balance * (1 + monthly_rate) ** self.koll_months
        return final_amount


class Bank:
    def __init__(self):
        self.clients = {}
        self.deposits = {}


    def register_client(self, client_id, name):
        self.clients[client_id] = name
        return f'Зарегистрирован клиент по имени {name} , и присвоен личный id {client_id}'


    def open_deposit_account(self, client_id, start_balance, years):
        if client_id in self.clients:
            self.deposits[client_id] = Deposit(start_balance, years)
            return f'Открыт депозитный счет по id: {client_id}, с балансом {start_balance} рублей на {years} лет'
        else:
            return f'Клиент с ID {client_id} не найден'


    def calc_deposit_interest_rate(self, client_id):
        if client_id in self.deposits:
            return self.deposits[client_id].calculate_final_amount()


    def close_deposit(self, client_id):
        if client_id in self.deposits:
            del self.deposits[client_id]
            return f'Депозитный счет закрыт'


bank = Bank()
client_id = "0000001"
name = "Siarhei"
start_balance = 1000
years = 1


print(bank.register_client(client_id, name))
print(bank.open_deposit_account(client_id, start_balance, years))
print(bank.calc_deposit_interest_rate(client_id))
print(bank.close_deposit(client_id))
print()
print()


# Task 2 Библиотека
class Book:
    def __init__(self, book_name, author, num_pages, isbn):
        self.book_name = book_name
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.reserv = None
        self.givenbook = None


    def reserve(self, Reader):
        if self.reserv is None:
            self.reserv = Reader
            return f'Книга {self.book_name} зарезервирована за {Reader.name}'
        else:
            return f'Книга уже заревервирована'


    def cancel_reserve(self, Reader):
        if self.reserv == Reader:
            self.reserv = None
            return f'Резервация на книгу {self.book_name} отменена'


    def get_book(self, Reader):
        if self.givenbook is None and self.reserv == Reader:
            self.givenbook = Reader
            self.reserv = None
            return f'Книга {self.book_name} выдана {Reader.name}'
        elif self.givenbook is not None:
            return f'Книга {self.book_name} уже выдана другому пользователю'
        else:
            return f'Вы не можете взять книгу, так как она не зарезервирована'


    def return_book(self, Reader):
        if self.givenbook == Reader:
            self.givenbook = None
            return f'Книга {self.book_name} возвращена {Reader.name}'
        else:
            return f'У вас нет книги'


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


book = Book("The Hobbit", "Books by J.R.R. Tolkien", 400, "0006754023")
vasya = Reader("Vasya")
petya = Reader("Petya")


print(vasya.reserve_book(book))
print(petya.reserve_book(book)) #<-- User can not reserve a book
print(vasya.cancel_reserve(book))
print(petya.reserve_book(book))
print(vasya.get_book(book)) #<-- User can not get a book
print(petya.get_book(book))
print(vasya.return_book(book)) #<-- User can not return a book
print(petya.return_book(book))
print(vasya.get_book(book))
