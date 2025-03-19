from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.detail import DetailView
from .models import Book, Library, UserProfile
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden
from .forms import BookForm, ExampleForm  # Import BookForm
from django.urls import reverse

@login_required
def admin_dashboard(request):
    try:
        # Get the logged-in user's profile
        user_profile = UserProfile.objects.get(user=request.user)
        
        # Check if the user is an Admin
        if user_profile.role == "Admin":
            return render(request, "admin_dashboard.html")  # Render the Admin page
        else:
            return HttpResponseForbidden("You are not authorized to view this page.")  # Restrict access
        
    except UserProfile.DoesNotExist:
        return HttpResponseForbidden("UserProfile not found. You are not authorized.")


# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Get all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})  # Pass books to the template

# Class-based view to show details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('list_books')  # Redirect to book list after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# User Login View
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_books')  # Redirect to book list after login
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# User Logout View
def user_logout(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

# ✅ Add Book View (Only for authorized users)
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        return render(request, 'relationship_app/add_book.html', {'form': form})
    return render(request, 'add_book.html', {'form': form})

# ✅ Edit Book View (Only for authorized users)
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})
    return render(request, 'edit_book.html', {'form': form, 'book': book})

# ✅ Delete Book View (Only for authorized users)
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
    return render(request, 'relationship_app/delete_book.html', {'book': book})
    return render(request, 'delete_book.html', {'book': book})

def search_books(request):
    title = request.GET.get('title', '')
    books = Book.objects.filter(title__icontains=title)
    return render(request, 'bookshelf/book_list.html', {'books': books})

def example_view(request):
    form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})