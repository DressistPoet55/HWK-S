import unittest
from HW12 import Book, Reader


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.book = Book("The Hobbit", "Books by J.R.R. Tolkien", 400, "0006754023")
        self.reader1 = Reader("Vasya")
        self.reader2 = Reader("Petya")

    def test_reserve_book(self):
        result = self.reader1.reserve_book(self.book)
        self.assertEqual(result, "Книга The Hobbit зарезервирована за Vasya")

    def test_reserve_already_reserved_book(self):
        self.reader1.reserve_book(self.book)
        result = self.reader2.reserve_book(self.book)
        self.assertEqual(result, "Книга уже заревервирована")

    def test_cancel_reserve(self):
        self.reader1.reserve_book(self.book)
        result = self.reader1.cancel_reserve(self.book)
        self.assertEqual(result, "Резервация на книгу The Hobbit отменена")

    def test_get_book(self):
        self.reader1.reserve_book(self.book)
        result = self.reader1.get_book(self.book)
        self.assertEqual(result, "Книга The Hobbit выдана Vasya")

    def test_get_book_not_reserved(self):
        result = self.reader1.get_book(self.book)
        self.assertEqual(result, "Вы не можете взять книгу, так как она не зарезервирована")

    def test_return_book(self):
        self.reader1.reserve_book(self.book)
        self.reader1.get_book(self.book)
        result = self.reader1.return_book(self.book)
        self.assertEqual(result, "Книга The Hobbit возвращена Vasya")

    def test_return_book_not_held(self):
        result = self.reader1.return_book(self.book)
        self.assertEqual(result, "У вас нет книги")

    @unittest.expectedFailure
    def test_get_book_reserved_by_another_user(self):
        self.reader1.reserve_book(self.book)
        result = self.reader2.get_book(self.book)
        self.assertEqual(result, "Книга The Hobbit выдана Vasya")  # Ожидаем ошибку


if __name__ == "__main__":
    unittest.main()
