from django.core.management.base import BaseCommand
from django.db import models
from library.models import Publisher

class Command(BaseCommand):
    help = 'Get addresses of publishers that occur most frequently'

    def handle(self, *args, **options):
        # Retrieve addresses of publishers and count their occurrences in the database
        addresses_frequency = Publisher.objects.values('address').annotate(address_count=models.Count('address')).order_by('-address_count')

        if addresses_frequency.exists():
            self.stdout.write(self.style.SUCCESS('Most frequently occurring publisher addresses:'))
            for idx, entry in enumerate(addresses_frequency, start=1):
                address = entry['address']
                count = entry['address_count']
                self.stdout.write(f"{idx}. Address: {address}, Occurrences: {count} times")
        else:
            self.stdout.write(self.style.WARNING('Publishers not found in the database.'))


#python manage.py publisher_command