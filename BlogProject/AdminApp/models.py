from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.contrib.auth import get_user_model
from django.conf import settings
# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=255)
    user_type_choices=[
        ('viewer', 'Viewer'),
        ('writer', 'Writer'),
    ]
    usertype = models.CharField(max_length=10, choices=user_type_choices, default='viewer')

class Blog(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="images",blank=True, null=True)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    def __str__(self):
        return self.title

    
