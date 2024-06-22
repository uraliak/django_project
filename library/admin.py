"""
Модуль для управления администрацией библиотеки с использованием Django admin и ImportExportModelAdmin.
"""

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Author, Book, Library, Publisher, Review, User
from .resources import (
    AuthorResource,
    BookResource,
    LibraryResource,
    PublisherResource,
    ReviewResource,
    UserResource,
)


class LibraryInline(admin.TabularInline):
    """
    Inline-админка для связи книг с библиотеками.
    """

    model = Book.library.through


class AuthorAdmin(ImportExportModelAdmin):
    """
    Администраторская модель для авторов с возможностью импорта/экспорта данных.
    """

    resource_class = AuthorResource
    list_display = ("id", "name", "email", "phone")
    list_filter = ("name", "email", "phone")
    date_hierarchy = "created_at"
    list_display_links = ("id", "name")
    search_fields = ("name", "email", "phone")
    export_order = ("id", "name", "email", "phone")
    ordering = ("id",)


class PublisherAdmin(ImportExportModelAdmin):
    """
    Администраторская модель для издателей с возможностью импорта/экспорта данных.
    """

    resource_class = PublisherResource
    list_display = ("id", "name", "address")
    list_filter = ("name", "address")
    date_hierarchy = "created_at"
    list_display_links = ("id", "name")
    search_fields = ("name", "address")
    export_order = ("id", "name", "address")
    ordering = ("id",)


class LibraryAdmin(ImportExportModelAdmin):
    """
    Администраторская модель для библиотек с возможностью импорта/экспорта данных.
    """

    resource_class = LibraryResource
    list_display = ("id", "name", "address")
    list_filter = ("name", "address")
    date_hierarchy = "created_at"
    list_display_links = ("id", "name")
    search_fields = ("name", "address")
    export_order = ("id", "name", "address")
    ordering = ("id",)


class LibraryFilter(admin.SimpleListFilter):
    """
    Фильтр для библиотеки в админке.
    """

    title = "library"
    parameter_name = "library"

    def lookups(self, request, model_admin):
        """
        Возвращает варианты для фильтрации по библиотекам.
        """

        libraries = Library.objects.all()
        return [(library.id, library.name) for library in libraries]

    def queryset(self, request, queryset):
        """
        Фильтрует queryset на основе выбранной библиотеки.
        """

        if self.value():
            return queryset.filter(library__id=self.value())
        return queryset


class BookAdmin(ImportExportModelAdmin):
    """
    Администраторская модель для книг с возможностью импорта/экспорта данных.
    """

    resource_class = BookResource
    list_display = ("id", "title", "author", "publisher", "get_libraries")
    list_filter = ("author", "publisher", LibraryFilter)
    inlines = [LibraryInline]
    filter_horizontal = ("library",)
    raw_id_fields = (
        "author",
        "publisher",
        "library",
    )
    export_order = ("id", "title", "author", "publisher", "get_libraries")
    ordering = ("id",)

    def get_libraries(self, obj):
        """
        Возвращает строку с названиями библиотек, в которых находится книга.
        """

        return ", ".join([library.name for library in obj.library.all()])

    get_libraries.short_description = "Libraries"
    date_hierarchy = "created_at"
    list_display_links = ("id", "title")
    readonly_fields = ("created_at",)
    search_fields = ("title", "author__name", "publisher__name", "library__name")


class UserAdmin(ImportExportModelAdmin):
    """
    Администраторская модель для пользователей с возможностью импорта/экспорта данных.
    """

    resource_class = UserResource
    list_display = ("id", "name", "email")
    list_filter = ("name", "email")
    date_hierarchy = "created_at"
    list_display_links = ("id", "name")
    search_fields = ("name", "email")
    export_order = ("id", "name", "email")
    ordering = ("id",)


class ReviewAdmin(ImportExportModelAdmin):
    """
    Администраторская модель для отзывов с возможностью импорта/экспорта данных.
    """

    resource_class = ReviewResource
    list_display = ("id", "book", "user", "rating", "comment")
    list_filter = ("book__title", "user", "rating")
    export_order = ("id", "book", "user", "rating", "comment")
    ordering = ("id",)

    def display_book(self, obj):
        """
        Возвращает название книги для отображения в админке.
        """

        return obj.book.title

    display_book.short_description = "Book"
    date_hierarchy = "created_at"
    list_display_links = ("id",)
    raw_id_fields = (
        "book",
        "user",
    )
    # readonly_fields = ('created_at',)
    # search_fields = ('book__title', 'user__name', 'comment')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Library, LibraryAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Review, ReviewAdmin)
