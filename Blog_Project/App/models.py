from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User


# Create your models here.

class CMSPages(models.Model):
    title = models.CharField(max_length=25)
    upload = models.ImageField(upload_to ='uploads/',null=True) 
    content = RichTextUploadingField()
    is_active = models.BooleanField()
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

class NewsEvent(models.Model):
    title = models.CharField(max_length=255)
    upload = models.ImageField(upload_to ='uploads/',null=True) 
    content = RichTextUploadingField()
    is_active = models.BooleanField()
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

class ContactUs(models.Model):
    name = models.CharField(max_length=255,null=False)
    email=  models.CharField(max_length=255,null=False)
    mobile = models.CharField(max_length=13,null=False)
    comment = models.TextField()
   
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

class Video(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.name)

class Blog(models.Model):
        user =  models.ForeignKey(User, on_delete=models.CASCADE)
        title= models.CharField(max_length=500)
        content = RichTextUploadingField()
        added = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
        def __str__(self):
            return str(self.title)
