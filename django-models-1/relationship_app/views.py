from django.shortcuts import render
from .models import Author, Book, Library, Librarian

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'relationship_app/author_list.html', {'authors': authors})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books})

def library_list(request):
    libraries = Library.objects.all()
    return render(request, 'relationship_app/library_list.html', {'libraries': libraries})

def librarian_detail(request, librarian_id):
    librarian = Librarian.objects.get(id=librarian_id)
    return render(request, 'relationship_app/librarian_detail.html', {'librarian': librarian})