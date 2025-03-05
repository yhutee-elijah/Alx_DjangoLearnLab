from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)  # Book title (max 200 characters)
    author = models.CharField(max_length=100)  # Author name (max 100 characters)
    publication_year = models.IntegerField()  # Year of publication

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"

