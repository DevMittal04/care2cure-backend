from django.db import models
from django.contrib.postgres.fields import ArrayField

import os
from uuid import uuid4
# Create your models here.

def path_and_rename(instance, filename):
    upload_to = 'media/images/users/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
 #   else:
        # set filename as random string
#      filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

def path_and_rename_counsellor(instance, filename):
    upload_to = 'media/images/counsellors/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.name:
        filename = '{}.{}'.format(instance.name, ext)
 #   else:
        # set filename as random string
#      filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

class User(models.Model):
    profile_pic = models.ImageField(upload_to=path_and_rename, null=True, blank=True, default='media/images/users/default_pic.png')
    email = models.EmailField(primary_key=True)
    name = models.CharField(max_length=64)
    dob = models.DateField()
    contact = models.BigIntegerField()
    address = models.CharField(max_length=254)
    acknowledgement = models.BooleanField(null=True, blank=True)
    occupation = models.CharField(max_length=64)
    marital_status = models.BooleanField(null=True, blank=True)
    password = models.CharField(max_length=32)

class Anonymous_User(models.Model):
    username = models.CharField(max_length=64, primary_key=True)
    dob = models.DateField()
    occupation = models.CharField(max_length=64)
    marital_status = models.BooleanField()

class Profile(models.Model):
    email = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    progress_file = models.FileField()
    counsellors_consulted = ArrayField(models.CharField(max_length=64))
    questions = ArrayField(models.CharField(max_length=64, blank=True))
    answers = ArrayField(models.CharField(max_length=64, blank=True))

class Anonymous_Profile(models.Model):
    username = models.OneToOneField(Anonymous_User, on_delete=models.CASCADE, primary_key=True)
    progress_file = models.FileField()
    counsellors_consulted = ArrayField(models.CharField(max_length=64, blank=True))
    questions = ArrayField(models.CharField(max_length=64, blank=True))
    answers = ArrayField(models.CharField(max_length=64, blank=True))

class Article(models.Model):
    email = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    desc = models.CharField(max_length=512,null=True)
    pic = models.ImageField(upload_to='images/articles',null=True, blank=True)
    title = models.CharField(max_length=64,null=True)

class Counsellor(models.Model):
    profile_pic = models.ImageField(upload_to=path_and_rename_counsellor)
    name = models.CharField(max_length=64)
    years_of_exp = models.IntegerField()
    occupation = models.CharField(max_length=64)
    ranking = models.IntegerField()
    contact = models.BigIntegerField()
    address = models.CharField(max_length=254)

class AgeMorbidityChart(models.Model):
    age = models.CharField(max_length=16)
    percentage = models.FloatField()

