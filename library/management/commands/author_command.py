from django.core.management.base import BaseCommand

from library.models import Author


class Command(BaseCommand):
    help = "Описание вашей команды"

    def handle(self, *args, **options):
        authors_with_name_starting_with_A = Author.objects.filter(name__startswith="A")
        self.stdout.write(
            self.style.SUCCESS(
                f"Found {authors_with_name_starting_with_A.count()} authors with names starting with A"
            )
        )


# python manage.py author_command
