from django.contrib import admin
from .models import Author, Publisher, Library, Book, User, Review

class LibraryInline(admin.TabularInline):
    model = Book.library.through

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_filter = ('name', 'email')
    date_hierarchy = 'created_at'
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email')

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address')
    list_filter = ('name', 'address')
    date_hierarchy = 'created_at'
    list_display_links = ('id', 'name')
    search_fields = ('name', 'address')

class LibraryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address')
    list_filter = ('name', 'address')
    date_hierarchy = 'created_at'
    list_display_links = ('id', 'name')
    search_fields = ('name', 'address')

class LibraryFilter(admin.SimpleListFilter):
    title = ('library')
    parameter_name = 'library'

    def lookups(self, request, model_admin):
        libraries = Library.objects.all()
        return [(library.id, library.name) for library in libraries]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(library__id=self.value())
        else:
            return queryset

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'publisher', 'get_libraries')
    list_filter = ('author', 'publisher', LibraryFilter)
    inlines = [LibraryInline]
    filter_horizontal = ('library',)
    raw_id_fields = ('author', 'publisher', 'library',)

    def get_libraries(self, obj):
        return ", ".join([library.name for library in obj.library.all()])

    get_libraries.short_description = 'Libraries'
    date_hierarchy = 'created_at'
    list_display_links = ('id', 'title')
    readonly_fields = ('created_at',)
    search_fields = ('title', 'author__name', 'publisher__name', 'library__name')

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_filter = ('name', 'email')
    date_hierarchy = 'created_at'
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'user', 'rating', 'comment')
    list_filter = ('book__title', 'user', 'rating')
    def display_book(self, obj):
        return obj.book.title
    
    display_book.short_description = 'Book'
    date_hierarchy = 'created_at'
    list_display_links = ('id',)
    raw_id_fields = ('book', 'user',)
    readonly_fields = ('created_at',)
    search_fields = ('book__title', 'user__name', 'comment')

    

admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Library, LibraryAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Review, ReviewAdmin)


