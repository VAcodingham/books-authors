from django.db import models

class Author(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    notes=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Book(models.Model):
    title=models.CharField(max_length=45)
    description=models.TextField()
    author=models.ManyToManyField(Author, related_name="books")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    

