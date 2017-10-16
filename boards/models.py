from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    name = models.Charfield(max_length=30, unique=True)
    description = models.CharField(maxlength=100)

class Topic(models.Model):
    subject = models.Charfield(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForiegnKey(Board, related_name='topics')
    starter = models.ForiegnKey(User, related_name='topics')

class Post(models.Model):
    message = message.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts')
    updated_by = models.ForeignKey(User, null=True, related_name='+')
    
# Create your models here.
