from django.shortcuts import render
from rest_framework import generics, permissions, serializers
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """Retrieve all books."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.allow_any]  # Allow any user to view the list of books\


class BookDetailView(generics.RetrieveAPIView):
    """Retrieve a single book by ID."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Allow any user to view book details

class BookCreateView(generics.CreateAPIView):
    """Add a new book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

def perform_create(self, serializer):
    """Ensure the publication year is not in the future before saving."""
    book = serializer.save()
    if book.publication_year > 2025:
        raise serializers.ValidationError({"publication_year": "Publication year cannot be in the future."}) 

class BookUpdateView(generics.UpdateAPIView):
    """Modify an existing book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    """Remove a book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
