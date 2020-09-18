# Generated by Django 3.0.8 on 2020-09-15 12:15

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anonymous_User',
            fields=[
                ('username', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('dob', models.DateField()),
                ('occupation', models.CharField(max_length=64)),
                ('marital_status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Counsellor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=64)),
                ('years_of_exp', models.IntegerField()),
                ('occupation', models.CharField(max_length=64)),
                ('ranking', models.IntegerField()),
                ('contact', models.IntegerField()),
                ('address', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('profile_pic', models.ImageField(upload_to='')),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('dob', models.DateField()),
                ('contact', models.IntegerField()),
                ('address', models.CharField(max_length=254)),
                ('acknowledgement', models.BooleanField()),
                ('occupation', models.CharField(max_length=64)),
                ('marital_status', models.BooleanField()),
                ('password', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Anonymous_Profile',
            fields=[
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='authentication.Anonymous_User')),
                ('progress_file', models.FileField(upload_to='')),
                ('counsellors_consulted', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=64), size=None)),
                ('questions', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=64), size=None)),
                ('answers', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=64), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('email', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='authentication.User')),
                ('desc', models.CharField(max_length=512)),
                ('pic', django.contrib.postgres.fields.ArrayField(base_field=models.ImageField(upload_to=''), size=None)),
                ('title', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('email', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='authentication.User')),
                ('progress_file', models.FileField(upload_to='')),
                ('counsellors_consulted', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=64), size=None)),
                ('questions', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=64), size=None)),
                ('answers', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=64), size=None)),
            ],
        ),
    ]