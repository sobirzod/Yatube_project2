from typing import AnyStr
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE

User = get_user_model()

class Group(models.Model):
    title = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(max_length=20, unique=True, null=False)
    description = models.TextField()

    def __str__(self) -> str:
        return self.slug


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        Group,
        on_delete=CASCADE, 
        blank=True,
        null=True,
        related_name='groups_posts'
    )



