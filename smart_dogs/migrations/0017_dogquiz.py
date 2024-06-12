# Generated by Django 5.0.1 on 2024-04-30 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_dogs', '0016_sectiondetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='DogQuiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('size', models.CharField(choices=[('small', 'Маленька'), ('medium', 'Середня'), ('large', 'Велика')], max_length=50)),
                ('skill_level', models.CharField(choices=[('beginner', 'Новачок'), ('intermediate', 'Любитель'), ('professional', 'Професіонал')], max_length=50)),
            ],
        ),
    ]
