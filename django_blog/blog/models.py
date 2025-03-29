from django.db import models
from django.contrib.auth.models import User, title, content, author, published_date   # Ensure this import is present

class Post(models.Model):
    title = models.CharField(max_length=200)  # Title field
    content = models.TextField()  # Content field
    published_date = models.DateTimeField(auto_now_add=True)  # Published date field
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Author field

    def __str__(self):
        return self.title  # Returns the title as a string representation
