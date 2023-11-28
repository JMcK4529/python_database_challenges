from lib.book import Book

def test_book_constructs():
    book = Book(1, "Test Title", "Fake Name")
    assert book.id == 1
    assert book.title == "Test Title"
    assert book.author_name == "Fake Name"

def test_book_to_string():
    book = Book(1, "Test Title", "Fake Name")
    assert str(book) == "Book(1, Test Title, Fake Name)"

def test_book_equality():
    book1 = Book(1, "Test Title", "Fake Name")
    book2 = Book(1, "Test Title", "Fake Name")
    assert book1 == book2