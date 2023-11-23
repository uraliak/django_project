from django.core.management.base import BaseCommand
from library.models import Book

class Command(BaseCommand):
    help = 'An example management command to demonstrate accessing related models.'

    def handle(self, *args, **options):
        # Your code here
        book_select = Book.objects.select_related('author').get(id=5) #title='1984'
        print(book_select.author.name)

        book_prefetch = Book.objects.prefetch_related('library').get(id=10)
        library = book_prefetch.library.all()
        print(library)

#python manage.py test_book