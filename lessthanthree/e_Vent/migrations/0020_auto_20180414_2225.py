# Generated by Django 2.0.2 on 2018-04-15 02:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_Vent', '0019_auto_20180413_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='saves',
            field=models.ManyToManyField(blank=True, related_name='saves', to=settings.AUTH_USER_MODEL),
        ),
    ]