# Generated by Django 3.2.5 on 2021-11-20 10:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0027_auto_20211113_1703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seminar',
            name='guest_description',
        ),
        migrations.RemoveField(
            model_name='seminar',
            name='guest_name',
        ),
        migrations.AddField(
            model_name='seminar',
            name='guidance',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='seminar',
            name='number_of_days',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='seminar',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hdhgfv', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='seminar',
            name='description',
            field=models.CharField(blank=True, max_length=555),
        ),
        migrations.AlterField(
            model_name='seminar',
            name='event_leader',
            field=models.CharField(blank=True, max_length=555),
        ),
        migrations.AlterField(
            model_name='seminar',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='seminar',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='seminar',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
