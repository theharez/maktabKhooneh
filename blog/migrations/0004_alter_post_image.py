# Generated by Django 4.1 on 2022-09-20 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='blog/default.jpg', upload_to='blog/'),
        ),
    ]