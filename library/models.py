from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords

class Author(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15, default='89990009900')
    def __str__(self):
        return self.name
    
    class Meta:
            verbose_name = 'Автор'
            verbose_name_plural = 'Авторы'

    history = HistoricalRecords()

class Publisher(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    def __str__(self):
        return self.name

    class Meta:
            verbose_name = 'Издатель'
            verbose_name_plural = 'Издатели'

    history = HistoricalRecords()

class Library(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
    class Meta:
            verbose_name = 'Библиотека'
            verbose_name_plural = 'Библиотеки'

    history = HistoricalRecords()

class Book(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    library = models.ManyToManyField(Library)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    history = HistoricalRecords()

class User(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    def __str__(self):
        return self.name
    
    class Meta:
            verbose_name = 'Пользователь'
            verbose_name_plural = 'Пользователи'

    history = HistoricalRecords()
    
class Review(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.CharField(max_length=500)
    def __str__(self):
        return f'{self.book.title} ({self.user.name})'
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    history = HistoricalRecords()


    
    
