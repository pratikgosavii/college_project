# Generated by Django 3.2.5 on 2021-10-26 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_event_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]