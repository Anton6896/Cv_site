# Generated by Django 3.1.2 on 2020-12-24 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mesage',
            name='slug',
        ),
    ]
