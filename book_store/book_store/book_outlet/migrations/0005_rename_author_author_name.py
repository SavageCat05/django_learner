# Generated by Django 5.0.6 on 2024-06-10 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0004_author_alter_book_author'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Author',
            new_name='author_name',
        ),
    ]
