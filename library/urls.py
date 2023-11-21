from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, PublisherViewSet, LibraryViewSet, BookViewSet, UserViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'publishers', PublisherViewSet, basename='publisher')
router.register(r'libraries', LibraryViewSet, basename='library')
router.register(r'books', BookViewSet, basename='book')
router.register(r'users', UserViewSet, basename='user')
router.register(r'reviews', ReviewViewSet, basename='review')

urlpatterns = router.urls

# from django.urls import path 
# from .views import AuthorListView, PublisherListView, LibraryListView, BookListView, UserListView, ReviewListView
# from .views import ReviewListView

# urlpatterns = [

#     # path('authors/', AuthorListView.as_view(), name='author_list'),
#     path('authors/', AuthorListView.as_view({'get': 'list', 'custom_list_action': 'custom_list_action', 'post': 'custom_detail_action'}), name='author_list'),

#     path('publishers/', PublisherListView.as_view({'get': 'list', 'custom_list_action': 'custom_list_action', 'post': 'custom_detail_action'}), name='publisher_list'), 

#     path('libraries/', LibraryListView.as_view({'get': 'list', 'custom_list_action': 'custom_list_action', 'post': 'custom_detail_action'}), name='library_list'), 

#     # path('books/', BookListView.as_view(), name='book_list'), 
#     path('books/', BookListView.as_view({'get': 'list', 'custom_list_action': 'custom_list_action', 'post': 'custom_detail_action'}), name='book_list'),


#     path('users/', UserListView.as_view({'get': 'list', 'custom_list_action': 'custom_list_action', 'post': 'custom_detail_action'}), name='user_list'), 

#     # path('reviews/', ReviewListView.as_view(), name='review_list'), 
#     path('reviews/', ReviewListView.as_view({'get': 'list', 'custom_list_action': 'custom_list_action', 'post': 'custom_detail_action'}), name='review_list'),

#     ]

