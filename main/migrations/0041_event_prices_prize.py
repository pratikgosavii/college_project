# Generated by Django 3.0.8 on 2022-01-29 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0040_auto_20220127_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='event_prices',
            name='prize',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
