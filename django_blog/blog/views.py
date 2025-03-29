from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import UserChangeForm
from .forms import RegisterForm

# User Registration
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", {"form": form})

# Profile View
@login_required
def profile_view(request):
    return render(request, "blog/profile.html")

# Custom Logout View
class CustomLogoutView(LogoutView):
    next_page = "login"  # Redirect to login page after logout

# User Profile Edit View
@login_required
def profile_edit_view(request):
    if request.method == "POST":
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, "blog/profile_edit.html", {"form": form})
