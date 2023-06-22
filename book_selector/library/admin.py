from django.contrib import admin
from .models import Author, Publisher, Library, Book, User, Review

admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Library)
admin.site.register(Book)
admin.site.register(User)
admin.site.register(Review)
