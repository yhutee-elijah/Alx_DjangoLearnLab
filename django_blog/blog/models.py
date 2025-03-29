from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)  # Title field
    content = models.TextField()  # Content field
    published_date = models.DateTimeField(auto_now_add=True)  # Published date field
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Author field

    def __str__(self):
        return self.title  # Returns the title as a string representation

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')  # Link to Post
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to User
    content = models.TextField()  # Comment content
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for updates

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"
