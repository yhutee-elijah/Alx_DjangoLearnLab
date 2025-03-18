from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Book 

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Display these fields in the admin list
    list_filter = ('publication_year', 'author')  # Add filtering options
    search_fields = ('title', 'author')  # Enable searching by title and author     


# Customize the admin panel for CustomUser
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Display these fields in the admin panel
    list_display = ('username', 'email', 'date_of_birth', 'is_staff', 'is_superuser')

    # Allow filtering by these fields
    list_filter = ('is_staff', 'is_superuser')

    # Customize the fieldsets to include additional fields
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

    # Customize the form for creating new users
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('username', 'email', 'password1', 'password2', 'date_of_birth', 'profile_photo')}),
    )

# Register the CustomUser model with CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)            


