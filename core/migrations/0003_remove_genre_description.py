# Generated by Django 4.2.7 on 2023-11-21 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_author_review_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='description',
        ),
    ]
