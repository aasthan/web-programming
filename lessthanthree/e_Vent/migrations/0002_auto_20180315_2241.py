# Generated by Django 2.0.2 on 2018-03-16 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('e_Vent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='e_Vent.Location'),
        ),
        migrations.AlterField(
            model_name='event',
            name='popularity',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='e_Vent.Popularity'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='price',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='e_Vent.Price'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='e_Vent.User'),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(help_text='Enter your event location (e.g. Umass, Mount Holyoke College).', max_length=500),
        ),
        migrations.AlterField(
            model_name='popularity',
            name='name',
            field=models.PositiveIntegerField(default=0, help_text='Popularity of the event'),
        ),
        migrations.AlterField(
            model_name='price',
            name='name',
            field=models.PositiveIntegerField(default=0, help_text='Enter your event price (e.g. 0, 5.5, 10).'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(help_text='Enter your event tag (e.g. cultural, sport).', max_length=30),
        ),
    ]
