from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
from posts.models import Post

# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(
        Post, 
        on_delete=models.CASCADE,
        related_name='comments',
    )
    comment = models.CharField(max_length=250)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment
    
    def get_absolute_url(self):
        return reverse("user_list")
    
    