# Generated by Django 4.2.2 on 2023-06-22 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0003_alter_book_library"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="library",
            field=models.ManyToManyField(
                blank=True, default=None, to="library.library"
            ),
        ),
    ]
