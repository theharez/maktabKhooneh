# Generated by Django 4.1 on 2022-10-09 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_alter_contact_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
