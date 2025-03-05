For each operation, I documented the commands in separate Markdown files (create.md, retrieve.md, update.md, delete.md).

I Created a Book (create.md)
Command:
from bookshelf.models import Book

# Create a book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Print the created book
print(book)
Expected Output 
1984 by George Orwell (1949)

Retrieve a Book (retrieve.md)
# Retrieve all books
books = Book.objects.all()
for book in books:
print(book)
Expected Output 
1984 by George Orwell (1949)

Update a Book (update.md)
# Retrieve the book
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()
# Print the updated book
print(book)
Expected Output 
Nineteen Eighty-Four by George Orwell (1949)

Delete a Book (delete.md)
# Retrieve the book
book = Book.objects.get(title="Nineteen Eighty-Four")
# Delete the book
book.delete()

# Try retrieving all books again
books = Book.objects.all()
print(list(books))
Expected Output (save in delete.md):
[]