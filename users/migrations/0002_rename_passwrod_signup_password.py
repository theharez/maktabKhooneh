# Generated by Django 4.1 on 2022-12-04 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='passwrod',
            new_name='password',
        ),
    ]
