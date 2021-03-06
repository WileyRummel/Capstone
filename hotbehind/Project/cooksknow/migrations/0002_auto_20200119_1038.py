# Generated by Django 2.2.7 on 2020-01-19 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooksknow', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='cuisines',
            field=models.ManyToManyField(to='cooksknow.Cuisine'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='settings',
            field=models.ManyToManyField(to='cooksknow.Setting'),
        ),
    ]
