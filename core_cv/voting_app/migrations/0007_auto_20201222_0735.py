# Generated by Django 3.1.2 on 2020-12-22 07:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('voting_app', '0006_auto_20201222_0716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votingchoices',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='votingchoices',
            name='voting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voting_class', to='voting_app.voting'),
        ),
    ]