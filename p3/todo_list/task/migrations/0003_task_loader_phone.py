# Generated by Django 5.0.6 on 2024-06-26 10:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_sign_in'),
    ]

    operations = [
        migrations.AddField(
            model_name='task_loader',
            name='phone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='task.sign_in'),
        ),
    ]
