# Generated by Django 2.2.7 on 2020-01-22 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200117_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('FOH', 'Front of house'), ('BOH', 'Back of house'), ('CHEF', 'Chef'), ('GM', 'General Manager')], max_length=4, null=True),
        ),
    ]
