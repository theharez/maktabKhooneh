# Generated by Django 4.1 on 2022-10-06 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.SmallIntegerField(null=True),
        ),
    ]
