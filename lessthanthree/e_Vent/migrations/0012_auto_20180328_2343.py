# Generated by Django 2.0.2 on 2018-03-29 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_Vent', '0011_auto_20180328_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='href',
            field=models.URLField(blank=True, default='https://www.google.com/', help_text='Input a link for this event'),
        ),
    ]
