import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django-models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.filter(name=author_name).first()
    if author:
        books = Book.objects.filter(author=author)
        return [book.title for book in books]
    return []

# List all books in a specific library
def get_library_by_name(library_name):
    library = Library.objects.filter(name=library_name).first()
    if library:
        return [book.title for book in library.books.all()]
    return []

# Retrieve the librarian for a library
def get_library_by_name(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian.name
    except Library.DoesNotExist:
        return None

# Example usage (assuming database has data)
if __name__ == "__main__":
    print("Books by J.K. Rowling:", get_books_by_author("J.K. Rowling"))
    print("Books in Central Library:", get_library_by_name("Central Library"))
    print("Librarian of City Library:", get_librarian_for_library("City Library"))
