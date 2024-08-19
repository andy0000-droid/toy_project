from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    nickname = models.CharField(max_length = 30)
    position = models.CharField(max_length = 30)
    subjects = models.CharField(max_length = 30)
    image = models.ImageField(upload_to='profile/', default = 'default.png')
    bio = models.TextField(blank=True, null=True)