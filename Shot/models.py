from distutils.command.upload import upload
from email.policy import default
from statistics import mode
from django.db import models

# Create your models here.
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_caption =models.CharField(default='',max_length=500,help_text="enter a caption")
    post_img = models.ImageField(upload_to='Websit/media',default='')
    def __str__(self):
        return self.post_caption 


class ContactUs(models.Model):
    first = models.CharField(max_length=30, null=True)
    last = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField()
    message = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.first