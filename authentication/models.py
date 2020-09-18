from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class User(models.Model):
<<<<<<< HEAD
    profile_pic = models.ImageField(upload_to='images/users/', null=True, blank=True)
=======
    profile_pic = models.ImageField(upload_to='images/users/',blank=True)
>>>>>>> c38e296d755c709215072727a24de593986b11a3
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
<<<<<<< HEAD
    pic = models.ImageField(upload_to='images/articles',null=True, blank=True)
=======
    pic1 = models.ImageField(upload_to='images/articles',null=True,blank=True)
    pic2 = models.ImageField(upload_to='images/articles',null=True,blank=True)
>>>>>>> c38e296d755c709215072727a24de593986b11a3
    title = models.CharField(max_length=64,null=True)





class Counsellor(models.Model):
    profile_pic = models.ImageField(upload_to='images/counsellors/')
    name = models.CharField(max_length=64)
    years_of_exp = models.IntegerField()
    occupation = models.CharField(max_length=64)
    ranking = models.IntegerField()
    contact = models.BigIntegerField()
    address = models.CharField(max_length=254)