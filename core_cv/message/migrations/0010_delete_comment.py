# Generated by Django 3.1.2 on 2020-12-26 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0009_comment_message'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]