# Generated by Django 3.0.8 on 2020-09-16 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_auto_20200916_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]