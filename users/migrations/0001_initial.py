# Generated by Django 4.1 on 2022-12-04 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('emial', models.EmailField(max_length=254)),
                ('passwrod', models.CharField(max_length=255)),
            ],
        ),
    ]
