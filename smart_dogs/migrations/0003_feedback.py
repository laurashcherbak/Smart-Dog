# Generated by Django 5.0.1 on 2024-01-24 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_dogs', '0002_entry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'feedbacks',
            },
        ),
    ]
