# Generated by Django 4.2.1 on 2023-05-24 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField(blank=True)),
                ('gender', models.CharField(max_length=25)),
                ('phone_number', models.IntegerField()),
                ('mail', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('department', models.CharField(max_length=200)),
                ('course', models.CharField(max_length=200)),
                ('purpose', models.CharField(max_length=200)),
                ('materials', models.TextField()),
            ],
        ),
    ]
