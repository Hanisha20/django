from typing import Any
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
# Create your models here.
class Post(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'posts')
    body = models.TextField()
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.slug} - {self.created}'
    
    def get_absolute_url(self):
        return reverse('homeApp:post_detail' , args = (self.id ,self.slug))
class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'ucomments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = 'pcomments')
    reply = models.ForeignKey('self', on_delete=models.CASCADE , related_name='rcomments', blank= True , null = True)
    is_reply = models.BooleanField(default=False)
    body = models.TextField(max_length= 400)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.body[:30]}'