# Generated by Django 3.0.8 on 2020-09-16 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0011_auto_20200916_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.User'),
        ),
    ]