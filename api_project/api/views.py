from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

class BookList (generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Define the BookViewSet for CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


