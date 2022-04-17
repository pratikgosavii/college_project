# Generated by Django 3.2.5 on 2021-11-24 19:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_auto_20211125_0114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='day_schedule',
            name='event',
        ),
        migrations.RemoveField(
            model_name='day_schedule',
            name='first_price_money',
        ),
        migrations.RemoveField(
            model_name='day_schedule',
            name='second_price_money',
        ),
        migrations.RemoveField(
            model_name='day_schedule',
            name='third_price_money',
        ),
        migrations.AddField(
            model_name='day_schedule',
            name='day',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sdsddsd', to='main.event_days'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='day_schedule',
            name='description',
            field=models.CharField(max_length=555, null=True),
        ),
        migrations.AddField(
            model_name='day_schedule',
            name='end_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='day_schedule',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='day_schedule',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='Event_Prices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_price_money', models.IntegerField(default=0)),
                ('second_price_money', models.IntegerField(default=0)),
                ('third_price_money', models.IntegerField(default=0)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sdsdsadc', to='main.event')),
            ],
        ),
    ]