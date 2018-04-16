# Generated by Django 2.0.2 on 2018-04-15 23:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('e_Vent', '0020_auto_20180414_2225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='popularity',
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(help_text='Write something about my event...', max_length=1000),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(help_text='Enter the ending date and time of your event', verbose_name='End Time'),
        ),
        migrations.AlterField(
            model_name='event',
            name='href',
            field=models.URLField(help_text='Link to my event is...', verbose_name='Link to the Event'),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.ForeignKey(help_text='This event is going to be at...', null=True, on_delete=django.db.models.deletion.CASCADE, to='e_Vent.Location'),
        ),
        migrations.AlterField(
            model_name='event',
            name='picture',
            field=models.ImageField(default='imgs/None/no-img.jpg', upload_to='imgs/', verbose_name='Upload Image'),
        ),
        migrations.AlterField(
            model_name='event',
            name='price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='e_Vent.Price', verbose_name='Entry Fee'),
        ),
        migrations.AlterField(
            model_name='event',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Organizer'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(help_text='Enter the starting date and time of your event', verbose_name='Start Time'),
        ),
        migrations.AlterField(
            model_name='event',
            name='tag',
            field=models.ManyToManyField(help_text='Please specify the category', to='e_Vent.Tag', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(help_text='The name for the event is...', max_length=100, verbose_name='Name of Event'),
        ),
    ]
