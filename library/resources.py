from import_export import resources
from .models import Author, Publisher, Library, Book, User, Review
from django.utils import timezone

class AuthorResource(resources.ModelResource):
    class Meta:
        model = Author

    def get_export_queryset(self, request=None):
        # Дополнительная кастомизация запроса перед экспортом
        return Author.objects.filter(created_at__lte=timezone.now())

    def get_created_at(self, author):
        # Дополнительная кастомизация значения поля "created_at" перед экспортом
        return timezone.localtime(author.created_at).strftime('%Y-%m-%d %H-%M-%S')

class PublisherResource(resources.ModelResource):
    class Meta:
        model = Publisher

class LibraryResource(resources.ModelResource):
    class Meta:
        model = Library

class BookResource(resources.ModelResource):
    class Meta:
        model = Book

    def dehydrate_author(self, book):
        return book.author.name if book.author else None

    def dehydrate_publisher(self, book):
        return book.publisher.name if book.publisher else None

    def dehydrate_library(self, book):
        return ", ".join([library.name for library in book.library.all()])

class UserResource(resources.ModelResource):
    class Meta:
        model = User

class ReviewResource(resources.ModelResource):
    class Meta:
        model = Review

    def dehydrate_book(self, review):
        return review.book.title if review.book else None

    def dehydrate_user(self, review):
        return review.user.name if review.user else None

   