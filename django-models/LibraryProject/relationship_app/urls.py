from django.shortcuts import path
from django.contrib.auth.views import LoginView, LogoutView 
from django.contrib.auth.decorators import User_passes_test
from .views import (
    register, #explicitly import register view
    list_books
    LibraryDetailView,
    user_login,
    user_logout,
    admin_view,
    librarian_view,
    member_view
)

def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'

def is_member (user):
    return user.is_authenticated and user.userprofile.role == 'Member'

urlpatterns = [
    path('register/', register, name='register'),  # User registration
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # Built-in login view
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # Built-in logout view
    path('books/', list_books, name='list_books'),  # Function-based view for books
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view for libraries
] 
