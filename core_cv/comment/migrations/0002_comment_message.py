# Generated by Django 3.1.2 on 2020-12-26 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0010_delete_comment'),
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='message',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='message.mesage'),
        ),
    ]
