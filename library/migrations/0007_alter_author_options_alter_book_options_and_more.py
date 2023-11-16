# Generated by Django 4.2.6 on 2023-11-11 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_author_created_at_book_created_at_library_created_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AlterModelOptions(
            name='library',
            options={'verbose_name': 'Библиотека', 'verbose_name_plural': 'Библиотеки'},
        ),
        migrations.AlterModelOptions(
            name='publisher',
            options={'verbose_name': 'Издатель', 'verbose_name_plural': 'Издатели'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]
