from django.core.management.base import BaseCommand
from library.models import Book

class Command(BaseCommand):
    help = 'Determine the author and publishers of a specific book'

    def add_arguments(self, parser):
        # Define the command-line argument for book title
        parser.add_argument('title', type=str, help='Title of the book to search for')

    def handle(self, *args, **options):
        # Get the title of the book from command-line arguments
        book_title = options['title']

        try:
            # Find the book in the database
            book = Book.objects.get(title__iexact=book_title)

            # Get the author
            author_name = book.author.name

            # Get the associated publisher(s)
            if hasattr(book, 'publisher') and callable(getattr(book.publisher, 'all', None)):
                # If 'publisher' is a ManyToManyField
                publishers = [publisher.name for publisher in book.publisher.all()]
            else:
                # If 'publisher' is a ForeignKey or another type
                publishers = [book.publisher.name] if hasattr(book, 'publisher') else []

            # Display the information
            self.stdout.write(self.style.SUCCESS(f'Book: {book_title}'))
            self.stdout.write(self.style.SUCCESS(f'Author: {author_name}'))
            self.stdout.write(self.style.SUCCESS(f'Publishers: {", ".join(publishers)}'))
        except Book.DoesNotExist:
            self.stdout.write(self.style.WARNING(f'Book with title "{book_title}" not found in the database.'))

#python manage.py book_command "Animal Farm" 