# Generated by Django 3.2.5 on 2021-11-24 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_seminar_day_schedule_seminar_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='first_price_money',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='second_price_money',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='third_price_money',
            field=models.IntegerField(default=0),
        ),
    ]
