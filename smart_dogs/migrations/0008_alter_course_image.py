# Generated by Django 5.0.1 on 2024-01-24 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_dogs', '0007_alter_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='smart_dogs/templates/smart_dogs/course_images/'),
        ),
    ]
