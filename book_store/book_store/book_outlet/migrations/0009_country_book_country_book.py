# Generated by Django 5.0.6 on 2024-06-10 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0008_alter_address_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('code', models.CharField(max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='country_book',
            field=models.ManyToManyField(to='book_outlet.country'),
        ),
    ]
