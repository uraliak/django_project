from django.views.generic.list import ListView 
from .models import Author, Publisher, Library, Book, User, Review


class AuthorListView(ListView): 
    model = Author
    template_name = 'author_list.html'

class PublisherListView(ListView): 
    model = Publisher 
    template_name = 'publisher_list.html'

class LibraryListView(ListView): 
    model = Library
    template_name = 'library_list.html'

class BookListView(ListView): 
    model = Book
    template_name = 'book_list.html'

class UserListView(ListView): 
    model = User
    template_name = 'user_list.html'

class ReviewListView(ListView): 
    model = Review
    template_name = 'review_list.html'
    