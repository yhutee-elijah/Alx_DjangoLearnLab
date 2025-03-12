from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library
from .models import Book, Library, UserProfile  # Import Book model
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseForbidden
from .models import UserProfile
from django.shortcuts import redirect

def is_admin(user):
    return user.is_authenticated and UserProfile.objects.get(user=user).role == "Admin"

@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_dashboard.html')
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
