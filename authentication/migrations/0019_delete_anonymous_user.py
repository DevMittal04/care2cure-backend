# Generated by Django 3.1.2 on 2020-11-17 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0018_chatbots_metadata'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Anonymous_User',
        ),
    ]