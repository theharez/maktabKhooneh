# Generated by Django 4.1 on 2022-10-04 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_category_post_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-published_data']},
        ),
    ]
