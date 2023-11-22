from django.core.management.base import BaseCommand
from library.models import Library

class Command(BaseCommand):
    help = 'Get the library associated with a specific address'

    def add_arguments(self, parser):
        # Define the command-line arguments
        parser.add_argument('address', nargs='+', type=str, help='The address to search for')

    def handle(self, *args, **options):
        # Get the address from command-line arguments
        address_to_search = ' '.join(options['address'])

        # Search for the library with the provided address
        try:
            library = Library.objects.get(address=address_to_search)
            self.stdout.write(self.style.SUCCESS(f'Library found with address "{address_to_search}": {library.name}'))
        except Library.DoesNotExist:
            self.stdout.write(self.style.WARNING(f'Library with address "{address_to_search}" not found in the database.'))


# python manage.py library_command "Ottawa, Canada" 