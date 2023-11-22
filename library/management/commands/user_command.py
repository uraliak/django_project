from django.core.management.base import BaseCommand
from library.models import User

class Command(BaseCommand):
    help = 'Retrieve the email of a user by name'

    def add_arguments(self, parser):
        # Define the command-line argument for user name
        parser.add_argument('name', type=str, help='Name of the user')

    def handle(self, *args, **options):
        # Get the name from command-line arguments
        user_name = options['name']

        try:
            # Find the user in the database
            user = User.objects.get(name__iexact=user_name)

            # Display the user's email
            self.stdout.write(self.style.SUCCESS(f'User: {user_name}'))
            self.stdout.write(self.style.SUCCESS(f'Email: {user.email}'))
        except User.DoesNotExist:
            self.stdout.write(self.style.WARNING(f'User with name "{user_name}" not found in the database.'))