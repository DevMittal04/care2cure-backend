# Generated by Django 3.1.2 on 2020-10-18 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_auto_20201016_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anonymous_user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
