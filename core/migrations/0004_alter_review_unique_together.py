# Generated by Django 4.2.7 on 2023-11-21 13:59

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_remove_genre_description'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('book', 'user')},
        ),
    ]
