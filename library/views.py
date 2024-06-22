from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters  # Готовые представления для наследования
from rest_framework import generics, serializers, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny  # Импорт прав доступа к представлению
from rest_framework.response import Response

from .models import Author, Book, Library, Publisher, Review, User
from .serializers import (
    AuthorSerializer,
    BookSerializer,
    LibrarySerializer,
    PublisherSerializer,
    ReviewSerializer,
    UserSerializer,
)


class AuthorViewSet(viewsets.ModelViewSet):
    model = Author
    template_name = "author_list.html"
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name", "email", "phone"]

    @action(methods=["GET"], detail=False)
    def custom_list_action(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serialized_data = self.get_serializer(queryset, many=True).data
        return Response({"message": "Custom List Action", "data": serialized_data})

    @action(methods=["POST"], detail=True)
    def custom_detail_action(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Custom Detail Action", "data": serializer.data})


class PublisherViewSet(viewsets.ModelViewSet):
    model = Publisher
    template_name = "publisher_list.html"
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = [
        AllowAny,
    ]
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "address"]

    def get_queryset(self):
        return Publisher.objects.filter(~Q(address__startswith="N"))

    @action(methods=["GET"], detail=False)
    def custom_list_action(self, request, *args, **kwargs):
        # Пример логики для дополнительного метода списка (GET)
        queryset = self.filter_queryset(self.get_queryset())
        serialized_data = self.get_serializer(queryset, many=True).data
        return Response({"message": "Custom List Action", "data": serialized_data})

    @action(methods=["POST"], detail=True)
    def custom_detail_action(self, request, *args, **kwargs):
        # Пример логики для дополнительного метода объекта (POST)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Custom Detail Action", "data": serializer.data})


class LibraryViewSet(viewsets.ModelViewSet):
    model = Library
    template_name = "library_list.html"
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    permission_classes = [
        AllowAny,
    ]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["name", "address"]

    @action(methods=["GET"], detail=False)
    def custom_list_action(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serialized_data = self.get_serializer(queryset, many=True).data
        return Response({"message": "Custom List Action", "data": serialized_data})

    @action(methods=["POST"], detail=True)
    def custom_detail_action(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Custom Detail Action", "data": serializer.data})


class BookViewSet(viewsets.ModelViewSet):
    model = Book
    template_name = "book_list.html"
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [
        AllowAny,
    ]
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "author__name", "publisher__name", "library__name"]

    @action(methods=["GET"], detail=False)
    def custom_list_action(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serialized_data = self.get_serializer(queryset, many=True).data
        return Response({"message": "Custom List Action", "data": serialized_data})

    @action(methods=["POST"], detail=True)
    def custom_detail_action(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Custom Detail Action", "data": serializer.data})


class UserViewSet(viewsets.ModelViewSet):
    model = User
    template_name = "user_list.html"
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        AllowAny,
    ]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["name", "email"]

    def get_queryset(self):
        return User.objects.filter(Q(email__startswith="j") | Q(email__startswith="m"))

    @action(methods=["GET"], detail=False)
    def custom_list_action(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serialized_data = self.get_serializer(queryset, many=True).data
        return Response({"message": "Custom List Action", "data": serialized_data})

    @action(methods=["POST"], detail=True)
    def custom_detail_action(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Custom Detail Action", "data": serializer.data})


class ReviewViewSet(viewsets.ModelViewSet):
    model = Review
    template_name = "review_list.html"
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [
        AllowAny,
    ]
    filter_backends = [filters.SearchFilter]
    search_fields = ["book__title", "user__name", "rating", "comment"]

    def get_queryset(self):
        return Review.objects.filter(
            Q(comment__startswith="A") & Q(rating__startswith="5")
        )

    @action(methods=["GET"], detail=False)
    def custom_list_action(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serialized_data = self.get_serializer(queryset, many=True).data
        return Response({"message": "Custom List Action", "data": serialized_data})

    @action(methods=["POST"], detail=True)
    def custom_detail_action(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Custom Detail Action", "data": serializer.data})
