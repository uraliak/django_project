from django.core.management.base import BaseCommand
from library.models import Review

class Command(BaseCommand):
    help = 'An example management command to demonstrate accessing related models.'

    def handle(self, *args, **options):
        # Your code here
        review_select = Review.objects.select_related('user').get(id=5)
        print(review_select.user.name)

#python manage.py test_review