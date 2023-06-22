from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Library(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    library = models.ManyToManyField(Library)

class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    def __str__(self):
        return self.name
    
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.CharField(max_length=500)


    
    
