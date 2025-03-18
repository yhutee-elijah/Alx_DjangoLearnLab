from django.db import models
from django.contrib.auth.models import AbstractUser
class Book(models.Model):
    title = models.CharField(max_length=200)  # Book title (max 200 characters)
    author = models.CharField(max_length=100)  # Author name (max 100 characters)
    publication_year = models.IntegerField()  # Year of publication

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
    
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

