from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
class Book(models.Model):
    title = models.CharField(max_length=200)  # Book title (max 200 characters)
    author = models.CharField(max_length=100)  # Author name (max 100 characters)
    publication_year = models.IntegerField()  # Year of publication
    isbn = models.CharField(max_length=13)

class Meta:
        permissions = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]

def __str__(self):
        return self.title 
    
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, date_of_birth=None, profile_photo=None):
        """
        Create and return a regular user with an email, username, and password.
        """
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, date_of_birth=date_of_birth, profile_photo=profile_photo)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        """
        Create and return a superuser with all permissions.
        """
        user = self.create_user(username=username, email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

 # Attach the custom manager
    objects = CustomUserManager()

    def __str__(self):
        return self.username