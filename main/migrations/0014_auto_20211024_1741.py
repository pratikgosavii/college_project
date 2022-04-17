# Generated by Django 3.2.5 on 2021-10-24 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_event_schedule_number_of_days'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event_schedule',
            name='number_of_days',
        ),
        migrations.AddField(
            model_name='event',
            name='number_of_days',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]