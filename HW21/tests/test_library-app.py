import pytest
import logging
from HW21.source.library import Book, Reader


logger = logging.getLogger()
file_handler = logging.FileHandler("library_test.log")
file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
logger.addHandler(file_handler)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
logger.addHandler(stream_handler)
logger.setLevel(logging.INFO)

@pytest.fixture
def library():
    book = Book("The Hobbit", "Books by J.R.R. Tolkien", 400, "0006754023")
    reader = Reader("Vasya")
    return book, reader


def test_reserve_book(library):
    logger.info("Тест резервирования книги")
    book, reader = library
    result = reader.reserve_book(book)
    assert result == "Книга The Hobbit зарезервирована за Vasya"


def test_cancel_reserve(library):
    logger.info("Тест отмены резервирования")
    book, reader = library
    reader.reserve_book(book)
    result = reader.cancel_reserve(book)
    assert result == "Резервация на книгу The Hobbit отменена"


@pytest.mark.xfail(reason="Книга уже зарезервирована")
def test_reserve_already_reserved_book(library):
    logger.warning("Тест резервирования уже зарезервированной книги")
    book, reader = library
    reader.reserve_book(book)
    second_reader = Reader("Petya")
    result = second_reader.reserve_book(book)
    assert result == "Книга The Hobbit зарезервирована за Petya"
