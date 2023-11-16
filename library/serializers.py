from rest_framework import serializers
from .models import Author, Publisher, Library, Book, User, Review

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
    
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Длина поля 'name' должна быть не менее 3 символов.")
        return value

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Длина поля 'title' должна быть не менее 3 символов.")
        return value

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Длина поля 'title' должна быть не менее 3 символов.")
        return value

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    publisher = PublisherSerializer()
    library = LibrarySerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'

    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Длина поля 'title' должна быть не менее 3 символов.")
        return value

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Длина поля 'title' должна быть не менее 3 символов.")
        return value

class ReviewSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    user = UserSerializer()

    class Meta:
        model = Review
        fields = '__all__'

    def validate_comment(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Длина поля 'title' должна быть не менее 3 символов.")
        return value