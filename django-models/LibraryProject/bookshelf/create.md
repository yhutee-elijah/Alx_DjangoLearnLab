from bookshelf.models import Book

# Create a book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Print the created book
print(book)
