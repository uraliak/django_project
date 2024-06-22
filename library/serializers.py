from rest_framework import serializers

from .models import Author, Book, Library, Publisher, Review, User


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

    fields_errors = {"blank": "Это поле не может быть пустым."}

    name = serializers.CharField(required=True, error_messages=fields_errors)
    email = serializers.EmailField(required=True, error_messages=fields_errors)
    phone = serializers.CharField(required=True, error_messages=fields_errors)

    def validate_name(self, value):
        if len(value) < 5:
            raise serializers.ValidationError(
                "Длина поля 'name' должна быть не менее 5 символов."
            )
        return value

    def validate_email(self, email):
        if not email.endswith("@mail.com"):
            raise serializers.ValidationError(
                "'email' должен быть на домене example.com"
            )
        return email


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = "__all__"

    fields_errors = {"blank": "Это поле не может быть пустым."}

    name = serializers.CharField(required=True, error_messages=fields_errors)
    address = serializers.CharField(required=True, error_messages=fields_errors)

    def validate_name(self, value):
        if len(value) < 5:
            raise serializers.ValidationError(
                "Длина поля 'name' должна быть не менее 5 символов."
            )
        return value


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = "__all__"

    fields_errors = {"blank": "Это поле не может быть пустым."}

    name = serializers.CharField(required=True, error_messages=fields_errors)
    address = serializers.CharField(required=True, error_messages=fields_errors)

    def validate_name(self, value):
        if len(value) < 10:
            raise serializers.ValidationError(
                "Длина поля 'name' должна быть не менее 10 символов."
            )
        return value


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    publisher = PublisherSerializer()
    library = LibrarySerializer(many=True)

    class Meta:
        model = Book
        fields = "__all__"

    fields_errors = {"blank": "Это поле не может быть пустым."}

    title = serializers.CharField(required=True, error_messages=fields_errors)

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError(
                "Длина поля 'title' должна быть не менее 5 символов."
            )
        return value


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    fields_errors = {"blank": "Это поле не может быть пустым."}

    name = serializers.CharField(required=True, error_messages=fields_errors)
    email = serializers.EmailField(required=True, error_messages=fields_errors)

    def validate_name(self, value):
        if len(value) < 5:
            raise serializers.ValidationError(
                "Длина поля 'name' должна быть не менее 5 символов."
            )
        return value

    def validate_email(self, email):
        if not email.endswith("@mail.com"):
            raise serializers.ValidationError("'email' должен быть на домене mail.com")
        return email


class ReviewSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    user = UserSerializer()

    class Meta:
        model = Review
        fields = "__all__"

    fields_errors = {
        "blank": "Это поле не может быть пустым.",
        "invalid": "Значение должно быть в диапазоне от 1 до 5.",
    }

    rating = serializers.IntegerField(required=True, error_messages=fields_errors)
    comment = serializers.CharField(required=True, error_messages=fields_errors)

    def validate_comment(self, value):
        if len(value) < 15:
            raise serializers.ValidationError(
                "Длина поля 'comment' должна быть не менее 15 символов."
            )
        return value

    def validate_rating(self, rate):
        if not (1 <= rate <= 5):
            raise serializers.ValidationError(
                "Значение поля 'rating' должно быть в диапазоне от 1 до 5."
            )
        return rate
