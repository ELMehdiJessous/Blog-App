from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tags(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Posts(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=300)
    tag = models.ManyToManyField(Tags)
    likes = models.ManyToManyField(User,related_name="liked_posts")
    
    def likes_number(self):
        return self.likes.count()
    
    def __str__(self):
        return self.title