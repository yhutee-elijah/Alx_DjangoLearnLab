# Retrieve all books
books = Book.objects.all()
for book in books:
    print(book)
