from django.urls import path 
from .views import AuthorListView, PublisherListView, LibraryListView, BookListView, UserListView, ReviewListView
from .views import ReviewListView

urlpatterns = [

    # path('authors/', AuthorListView.as_view(), name='author_list'),
    path('authors/', AuthorListView.as_view({'get': 'list', 'custom_list_action': 'custom_list_action'}), name='author_list'),

    path('publishers/', PublisherListView.as_view(), name='publisher_list'), 

    path('libraries/', LibraryListView.as_view(), name='library_list'), 

    # path('books/', BookListView.as_view(), name='book_list'), 
    path('books/', BookListView.as_view({'get': 'list', 'custom_list_action': 'custom_list_action'}), name='book_list'),


    path('users/', UserListView.as_view(), name='user_list'), 

    # path('reviews/', ReviewListView.as_view(), name='review_list'), 
    path('reviews/', ReviewListView.as_view({'get': 'list', 'custom_list_action': 'custom_list_action'}), name='review_list'),

    ]