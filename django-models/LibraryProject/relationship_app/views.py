from django.shortcuts import render
from .models import Book  # Import Book model

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Get all books from the database
    return render(request, 'list_books.html', {'books': books})

from django.views.generic import DetailView
from .models import Library

# Class-based view to show details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
