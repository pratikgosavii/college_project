# Generated by Django 3.2.5 on 2021-10-25 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20211025_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_leader',
            field=models.CharField(max_length=555),
        ),
    ]