# Generated by Django 4.2.7 on 2023-11-21 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_book_authors_remove_book_genres_book_author_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='biography',
        ),
    ]