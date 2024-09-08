from django.db import models
import uuid
from .templatetags import filters
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("home")
    
categories=Category.objects.all().values_list('name','name')
categories_list=[]
for child in categories:
    categories_list.append(child)

class Account(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name= models.CharField(max_length=255)
    birthday = models.DateTimeField()
    avatar=models.ImageField(upload_to='user-avatars/',null=True,blank=True,default='/user-avatars/no-avatar.jpg')
    address=models.CharField(max_length=255, null=True, blank=True)
    joined_on=models.DateTimeField(auto_now_add=True, null=False)
    
    def __str__(self):
        return f"{self.name}"
    
class Post(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author=models.CharField(max_length=255)
    body=models.TextField()
    post_date=models.DateField(auto_now_add=True)
    image=models.ImageField(upload_to='post-images/',null=True,blank=True)
    category=models.CharField(default="",max_length=255,choices=categories_list,blank=True)
    def __str__(self):
        return f"{self.author} | {self.body}"

    def get_absolute_url(self):
        return reverse('home')
    
class Comment(models.Model):
    post=models.ForeignKey(Post, related_name="comments",  on_delete=models.CASCADE)
    name=models.CharField(max_length=255,blank=True)
    body=models.TextField()
    date_commented=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return '%s - %s' %(self.post.body, self.name)