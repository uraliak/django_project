import random

from django.core.management.base import BaseCommand

from library.models import Review


class Command(BaseCommand):
    help = "Get a random quote from reviews"

    def handle(self, *args, **options):
        # Получаем все отзывы из базы данных
        reviews = Review.objects.all()

        if reviews.exists():
            # Выбираем случайный отзыв
            random_review = random.choice(reviews)

            # Выводим цитату из выбранного отзыва
            quote = random_review.comment[:50]  # Возьмем первые 50 символов комментария
            self.stdout.write(self.style.SUCCESS(f'Random Quote: "{quote}"'))
        else:
            self.stdout.write(self.style.WARNING("No reviews found in the database."))


# python manage.py review_command
