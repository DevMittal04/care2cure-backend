# Generated by Django 3.1.1 on 2020-09-29 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_suicidalriskchart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suicidalriskchart',
            name='group',
            field=models.CharField(max_length=32),
        ),
    ]