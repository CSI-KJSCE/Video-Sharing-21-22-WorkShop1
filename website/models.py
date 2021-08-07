from django.db import models
from django.db.models.fields import CharField, TextField

from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
# Create your models here.

def __str__(self):
    return self.user.username

'''
class User(models.Model):

    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True, primary_key=True)
    emailID = models.EmailField(unique=True)
    pfp = models.ImageField()



    def __str__(self):
        return self.username
'''
'''
class Video(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE,default="")
    title = models.CharField(max_length=100,default="")
    description = TextField(max_length=1000,default="")
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    thumbnail = models.ImageField(default = None)
    video = models.FileField(upload_to='videos_uploaded',validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])], default=None)

    #thumbnail= models.ImageField()

    def __str__(self):
        return self.title
'''

class NewVideo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default="")
    title = models.CharField(max_length=100,default="")
    description = TextField(max_length=1000,default="")
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    date = models.CharField(default="",max_length=100)
    thumbnail = models.ImageField(default = None)
    video = models.FileField(upload_to='videos_uploaded',validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])], default=None)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default="")
    text = models.TextField(max_length=1000,default="")

    def __str__(self):
        return text
