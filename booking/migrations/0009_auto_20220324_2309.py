# Generated by Django 3.0.8 on 2022-03-24 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0043_feedback_questions'),
        ('booking', '0008_auto_20220323_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='feeback_questions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='efesfszsfwe', to='main.feedback_questions'),
        ),
        migrations.DeleteModel(
            name='feedback_questions',
        ),
    ]