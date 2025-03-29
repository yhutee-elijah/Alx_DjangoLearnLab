from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from api.models import Author, Book
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):
    """Test cases for the Book API endpoints."""

    def setUp(self):
        """Set up test data before running each test."""
        self.user = User.objects.create_user(username="testuser", password="testpassword")

        self.author = Author.objects.create(name="J.K. Rowling")
        self.book1 = Book.objects.create(title="Harry Potter", publication_year=1997, author=self.author)
        self.book2 = Book.objects.create(title="Fantastic Beasts", publication_year=2016, author=self.author)

        self.client.login(username="testuser", password="testpassword")

    ## 📝 Test: List all books
    def test_list_books(self):
        url = reverse('book-list')  # Uses the name from urls.py
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # We created 2 books

    ## 📝 Test: Retrieve a single book
    def test_retrieve_book(self):
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Harry Potter")

    ## 📝 Test: Create a new book (Authenticated user)
    def test_create_book_authenticated(self):
        url = reverse('book-create')
        data = {"title": "New Book", "publication_year": 2023, "author": self.author.id}
        self.client.force_authenticate(user=self.user)  # Ensure authentication
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)  # 2 from setup + 1 new

    ## 📝 Test: Unauthorized book creation
    def test_create_book_unauthenticated(self):
        url = reverse('book-create')
        data = {"title": "Unauthorized Book", "publication_year": 2023, "author": self.author.id}
        self.client.logout()
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Should be forbidden

    ## 📝 Test: Update a book
    def test_update_book(self):
        url = reverse('book-update', args=[self.book1.id])
        data = {"title": "Harry Potter Updated", "publication_year": 1997, "author": self.author.id}
        self.client.force_authenticate(user=self.user)
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Harry Potter Updated")

    ## 📝 Test: Delete a book
    def test_delete_book(self):
        url = reverse('book-delete', args=[self.book2.id])
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)  # Only 1 book should remain

    ## 📝 Test: Filtering books by title
    def test_filter_books_by_title(self):
        url = reverse('book-list') + "?title=Harry Potter"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Harry Potter")

    ## 📝 Test: Search books by author name
    def test_search_books_by_author(self):
        url = reverse('book-list') + "?search=Rowling"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    ## 📝 Test: Ordering books by publication year (ascending)
    def test_order_books_by_publication_year_asc(self):
        url = reverse('book-list') + "?ordering=publication_year"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 1997)  # Oldest first

    ## 📝 Test: Ordering books by publication year (descending)
    def test_order_books_by_publication_year_desc(self):
        url = reverse('book-list') + "?ordering=-publication_year"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2016)  # Newest first

