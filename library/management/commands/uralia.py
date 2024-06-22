from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Описание вашей команды"

    def handle(self, *args, **kwargs):
        print("Hello, I am Uralia. Welcome to my code space")
