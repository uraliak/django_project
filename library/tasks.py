from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from library.models import Book, User


def get_weeks_best_books():
    best_books = Book.objects.all()[:10]
    return best_books


def send_weekly_best_books_email():
    users = User.objects.all()
    books = get_weeks_best_books()
    for user in users:
        subject = "Самые популярные книги недели!"
        html_message = render_to_string(
            "emails/weekly_best_books.html", {"books": books, "user": user}
        )
        plain_message = strip_tags(html_message)
        from_email = settings.EMAIL_HOST_USER
        to = user.email

        send_mail(subject, plain_message, from_email, [to], html_message=html_message)


@shared_task
def weekly_best_books_email_task():
    send_weekly_best_books_email()
