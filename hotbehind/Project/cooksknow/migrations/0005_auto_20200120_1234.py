# Generated by Django 2.2.7 on 2020-01-20 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cooksknow', '0004_auto_20200120_1124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='restaurantrev',
            new_name='restaurant',
        ),
    ]
