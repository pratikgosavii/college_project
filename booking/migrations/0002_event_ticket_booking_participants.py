# Generated by Django 3.2.5 on 2021-10-15 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event_ticket_booking',
            name='participants',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]
