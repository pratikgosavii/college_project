# Generated by Django 3.0.8 on 2022-04-19 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QrCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('image', models.ImageField(blank=True, upload_to='qrcode')),
            ],
        ),
    ]
