from django.urls import path 
from .views import AuthorListView, PublisherListView, LibraryListView, BookListView, UserListView, ReviewListView

urlpatterns = [ 
    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('publishers/', PublisherListView.as_view(), name='publisher_list'), 
    path('libraries/', LibraryListView.as_view(), name='library_list'), 
    path('books/', BookListView.as_view(), name='book_list'), 
    path('users/', UserListView.as_view(), name='user_list'), 
    path('reviews/', ReviewListView.as_view(), name='review_list'),  
    ]

