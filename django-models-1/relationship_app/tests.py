from django.test import TestCase
from .models import Author, Book, Library, Librarian

class AuthorModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="J.K. Rowling")

    def test_author_creation(self):
        self.assertEqual(self.author.name, "J.K. Rowling")

class BookModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book = Book.objects.create(title="Harry Potter", author=self.author)

    def test_book_creation(self):
        self.assertEqual(self.book.title, "Harry Potter")
        self.assertEqual(self.book.author.name, "J.K. Rowling")

class LibraryModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book1 = Book.objects.create(title="Harry Potter", author=self.author)
        self.book2 = Book.objects.create(title="The Casual Vacancy", author=self.author)
        self.library = Library.objects.create(name="City Library")
        self.library.books.add(self.book1, self.book2)

    def test_library_books(self):
        self.assertEqual(self.library.books.count(), 2)

class LibrarianModelTest(TestCase):
    def setUp(self):
        self.library = Library.objects.create(name="City Library")
        self.librarian = Librarian.objects.create(name="Alice", library=self.library)

    def test_librarian_creation(self):
        self.assertEqual(self.librarian.name, "Alice")
        self.assertEqual(self.librarian.library.name, "City Library")