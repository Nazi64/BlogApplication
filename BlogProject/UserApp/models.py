from django.db import models
from django.contrib.auth.models import User
from AdminApp.models import Blog
from django.conf import settings
# Create your models here.

class Comment(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    description=models.TextField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)  

    
    
