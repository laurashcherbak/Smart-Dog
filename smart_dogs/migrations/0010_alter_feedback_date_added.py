# Generated by Django 5.0.1 on 2024-01-26 17:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_dogs', '0009_entry_owner_feedback_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]