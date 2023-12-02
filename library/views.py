from rest_framework import generics, serializers, viewsets  # Готовые представления для наследования
from rest_framework.permissions import AllowAny  # Импорт прав доступа к представлению

from .models import Author, Publisher, Library, Book, User, Review
from .serializers import AuthorSerializer, PublisherSerializer, LibrarySerializer, BookSerializer, UserSerializer, ReviewSerializer

from django.db.models import Q

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from rest_framework.decorators import action

from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

# from django.views.generic.list import ListView 

class AuthorViewSet(viewsets.ModelViewSet): # (viewsets.ModelViewSet, ListView, generics.ListCreateAPIView) AuthorListView
    model = Author
    template_name = 'author_list.html'
    queryset = Author.objects.all()  # Данные с которыми хотим производить манипуляции
    serializer_class = AuthorSerializer  # Класс сериализации для валидации и сериализации данных
    permission_classes = [AllowAny, ]  # Права доступа к представлению. AllowAny - доступ открыт для всех
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'email', 'phone']

    # def get_queryset(self):
    #     return Author.objects.filter(Q(name__startswith='J') | Q(email__startswith='g')) 

    @action(methods=['GET'], detail=False)
    def custom_list_action(self, request, *args, **kwargs):
        # Пример логики для дополнительного метода списка (GET)
        queryset = self.filter_queryset(self.get_queryset())
        serialized_data = self.get_serializer(queryset, many=True).data
        return Response({"message": "Custom List Action", "data": serialized_data})

    @action(methods=['POST'], detail=True)
    def custom_detail_action(self, request, *args, **kwargs):
        # Пример логики для дополнительного метода объекта (POST)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Custom Detail Action", "data": serializer.data})

class PublisherViewSet(viewsets.ModelViewSet): # (ListView, generics.ListCreateAPIView)
    model = Publisher 
    template_name = 'publisher_list.html'
    queryset = Publisher.objects.all()  # Данные с которыми хотим производить манипуляции
    # queryset = Book.objects.filter(Q(publisher__address__icontains='New York, USA')) #| Q(publisher__name__icontains='Wiley')
    serializer_class = PublisherSerializer  # Класс сериализации для валидации и сериализации данных
    permission_classes = [AllowAny, ]  # Права доступа к представлению. AllowAny - доступ открыт для всех
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'address']

    def get_queryset(self):
        return Publisher.objects.filter(~Q(address__startswith='N'))

    @action(methods=['GET'], detail=False)
    def custom_list_action(self, request, *args, **kwargs):
        # Пример логики для дополнительного метода списка (GET)
        queryset = self.filter_queryset(self.get_queryset())
        serialized_data = self.get_serializer(queryset, many=True).data
        return Response({"message": "Custom List Action", "data": serialized_data})

    @action(methods=['POST'], detail=True)
    def custom_detail_action(self, request, *args, **kwargs):
        # Пример логики для дополнительного метода объекта (POST)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Custom Detail Action", "data": serializer.data})

class LibraryViewSet(viewsets.ModelViewSet): # (ListView, generics.ListCreateAPIView)
    model = Library
    template_name = 'library_list.html'
    queryset = Library.objects.all()  # Данные с которыми хотим производить манипуляции
    serializer_class = LibrarySerializer  # Класс сериализации для валидации и сериализации данных
    permission_classes = [AllowAny, ]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name', 'address']

    # def get_queryset(self):
    #     return Library.objects.filter(Q(name__startswith='B') | Q(name__startswith='L'))

    @action(methods=['GET'], detail=False)
    def custom_list_action(self, request, *args, **kwargs):
        # Пример логики для дополнительного метода списка (GET)
        queryset = self.filter_queryset(self.get_queryset())
        serialized_data = self.get_serializer(queryset, many=True).data
        return Response({"message": "Custom List Action", "data": serialized_data})

    @action(methods=['POST'], detail=True)
    def custom_detail_action(self, request, *args, **kwargs):
        # Пример логики для дополнительного метода объекта (POST)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Custom Detail Action", "data": serializer.data})

      # Права доступа к представлению. AllowAny - доступ открыт для всех

class BookViewSet(viewsets.ModelViewSet): # (ListView, generics.ListCreateAPIView)
    model = Book
    template_name = 'book_list.html'
    queryset = Book.objects.all()
    # queryset = Book.objects.all()  # Данные с которыми хотим производить манипуляции
    # queryset = Book.objects.filter(Q(title__icontains='1984') | Q(author__name__icontains='William Golding') | Q(publisher__name__icontains = 'HarperCollins'))
    serializer_class = BookSerializer # Класс сериализации для валидации и сериализации данных
    permission_classes = [AllowAny, ]  # Права доступа к представлению. AllowAny - доступ открыт для всех
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author__name', 'publisher__name', 'library__name']
    
    # def get_queryset(self):
    #     return Book.objects.filter(Q(title__startswith='T') & ~Q(publisher__name='HarperCollins'))
        
    @action(methods=['GET'], detail=False)
    def custom_list_action(self, request, *args, **kwargs):
        # Пример логики для дополнительного метода списка (GET)
        queryset = self.filter_queryset(self.get_queryset())
        serialized_data = self.get_serializer(queryset, many=True).data
        return Response({"message": "Custom List Action", "data": serialized_data})

    @action(methods=['POST'], detail=True)
    def custom_detail_action(self, request, *args, **kwargs):
        # Пример логики для дополнительного метода объекта (POST)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Custom Detail Action", "data": serializer.data})

class UserViewSet(viewsets.ModelViewSet): # (ListView, generics.ListCreateAPIView)
    model = User
    template_name = 'user_list.html'
    queryset = User.objects.all()  # Данные с которыми хотим производить манипуляции
    serializer_class = UserSerializer  # Класс сериализации для валидации и сериализации данных
    permission_classes = [AllowAny, ]  # Права доступа к представлению. AllowAny - доступ открыт для всех
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name', 'email']

    def get_queryset(self):
        return User.objects.filter(Q(email__startswith='j') | Q(email__startswith='m'))

    @action(methods=['GET'], detail=False)
    def custom_list_action(self, request, *args, **kwargs):
        # Пример логики для дополнительного метода списка (GET)
        queryset = self.filter_queryset(self.get_queryset())
        serialized_data = self.get_serializer(queryset, many=True).data
        return Response({"message": "Custom List Action", "data": serialized_data})

    @action(methods=['POST'], detail=True)
    def custom_detail_action(self, request, *args, **kwargs):
        # Пример логики для дополнительного метода объекта (POST)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Custom Detail Action", "data": serializer.data})

class ReviewViewSet(viewsets.ModelViewSet): # (ListView, generics.ListCreateAPIView)
    model = Review
    template_name = 'review_list.html'
    queryset = Review.objects.all()  # Данные с которыми хотим производить манипуляции
    # queryset = Book.objects.filter(Q(review__rating__icontains='5') | Q(title__icontains='To Kill a Mockingbird')) #| Q(review__user__name__icontains = 'Sarah Taylor')
    serializer_class = ReviewSerializer  # Класс сериализации для валидации и сериализации данных
    permission_classes = [AllowAny, ]  # Права доступа к представлению. AllowAny - доступ открыт для всех
    filter_backends = [filters.SearchFilter]
    search_fields = ['book__title', 'user__name', 'rating', 'comment']

    def get_queryset(self):
        return Review.objects.filter(Q(comment__startswith='A') & Q(rating__startswith='5'))

    @action(methods=['GET'], detail=False)
    def custom_list_action(self, request, *args, **kwargs):
        # Пример логики для дополнительного метода списка (GET)
        queryset = self.filter_queryset(self.get_queryset())
        serialized_data = self.get_serializer(queryset, many=True).data
        return Response({"message": "Custom List Action", "data": serialized_data})
    
    @action(methods=['POST'], detail=True)
    def custom_detail_action(self, request, *args, **kwargs):
        # Пример логики для дополнительного метода объекта (POST)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Custom Detail Action", "data": serializer.data})
    