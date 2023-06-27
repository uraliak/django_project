from django.db import models
from django.utils import timezone

class Author(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    def __str__(self):
        return self.name

class Publisher(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Library(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Book(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    library = models.ManyToManyField(Library)
    def __str__(self):
        return self.title

class User(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    def __str__(self):
        return self.name
    
class Review(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.CharField(max_length=500)
    def __str__(self):
        return f'{self.book.title} ({self.user.name})'


    
    
