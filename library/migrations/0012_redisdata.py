# Generated by Django 4.2.6 on 2024-06-21 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0011_alter_author_phone_alter_historicalauthor_phone"),
    ]

    operations = [
        migrations.CreateModel(
            name="RedisData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("key", models.CharField(max_length=255, unique=True)),
                ("value", models.TextField()),
            ],
        ),
    ]
