# Generated by Django 2.0.2 on 2018-04-13 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('e_Vent', '0015_auto_20180408_2013'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('picture', models.ImageField(default='imgs/None/no-img.jpg', upload_to='imgs/')),
                ('contact', models.CharField(help_text='Enter your email address or phone number.', max_length=100)),
                ('bio', models.TextField(help_text='Enter a brief description of you/your organization.', max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='event',
        ),
        migrations.RemoveField(
            model_name='event',
            name='user',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='profile',
            name='event',
            field=models.ManyToManyField(related_name='_profile_event_+', to='e_Vent.Event'),
        ),
        migrations.AddField(
            model_name='event',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='e_Vent.Profile'),
        ),
    ]
