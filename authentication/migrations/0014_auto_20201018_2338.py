# Generated by Django 3.1.2 on 2020-10-18 18:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0013_auto_20201018_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentalstates',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
