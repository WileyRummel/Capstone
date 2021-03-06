# Generated by Django 2.2.7 on 2020-01-24 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooksknow', '0011_auto_20200122_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='hours',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='photo',
            field=models.ImageField(default='images/default.jpg', upload_to='images'),
        ),
    ]
