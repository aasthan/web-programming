# Generated by Django 2.0.2 on 2018-04-13 16:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('e_Vent', '0018_event_saves'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
