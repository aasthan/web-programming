# Generated by Django 2.0.2 on 2018-03-29 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_Vent', '0008_auto_20180327_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='popularity',
            name='name',
            field=models.IntegerField(default=0, help_text='Popularity of the event'),
        ),
    ]