from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books, LibraryDetailView, register, user_login, user_logout

def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'

urlpatterns = [
    path('register/', views.register, name='register'),  # User registration
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # Built-in login view
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # Built-in logout view
    path('books/', list_books, name='list_books'),  # Function-based view for books
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view for libraries
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),  # ✅ Admin-only view
]


