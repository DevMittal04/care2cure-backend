from django.db import models
from django.contrib.postgres.fields import ArrayField

#from .libra import DictionaryField
import os
from uuid import uuid4
from django.utils import timezone
import datetime
#from json_field import JSONField
from django.contrib.postgres.fields import JSONField

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
 #
    acknowledgement = models.BooleanField(null=True, blank=True)
    occupation = models.CharField(max_length=64)
 #
    marital_status = models.BooleanField(null=True, blank=True)
    password = models.CharField(max_length=32)

    def __str__(self):
        return str(self.email)
#
# class Anonymous_User(models.Model):
#     id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=64, null=True, blank=True)
    
#     def __str__(self):
#         return str(self.id)

#
# class Profile(models.Model):
#     email = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     counsellors_consulted = ArrayField(models.CharField(max_length=64),blank=True)

class MentalStates(models.Model):
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.CharField(max_length=16)
    datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.email)

class Article(models.Model):
    email = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    desc = models.CharField(max_length=512,null=True)
#
    pic = models.ImageField(upload_to='images/articles',null=True, blank=True)
    title = models.CharField(max_length=64,null=True)

    def __str__(self):
        return self.title

class Counsellor(models.Model):
    profile_pic = models.ImageField(upload_to=path_and_rename_counsellor)
    name = models.CharField(max_length=64)
    years_of_exp = models.IntegerField()
    occupation = models.CharField(max_length=64)
    ranking = models.IntegerField()
    contact = models.BigIntegerField()
    address = models.CharField(max_length=254)

    def __str__(self):
        return self.name

class AgeMorbidityChart(models.Model):
    age = models.CharField(max_length=16)
    percentage = models.FloatField()

class StateDisorderChart(models.Model):
    state = models.CharField(max_length=16)
    percentage = models.FloatField()

class SuicidalRiskChart(models.Model):
    group = models.CharField(max_length=32)
    percentage = models.FloatField()

class HumanResourcesChart(models.Model):
    state = models.CharField(max_length=16)
    psychiatrist = models.FloatField()
    psychologist = models.FloatField()
    social_workers = models.FloatField()

class ChatBots(models.Model):
    key = models.CharField(max_length=64)
    groupId = models.BigIntegerField()
    clientGroupId = models.CharField(max_length=16)
    message = models.CharField(max_length=512)
    email = models.EmailField(blank=True, null=True)
    metadata = JSONField(null=True, blank=True)

    def __str__(self):
        return self.message
    