# Generated by Django 3.1.2 on 2020-12-26 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'custom_user', 'verbose_name_plural': 'custom_users'},
        ),
        migrations.AlterModelTable(
            name='customuser',
            table='CustomUser',
        ),
    ]
