from django.db import models

from django.contrib.auth.models import User                        # -5a
from django.utils import timezone

# Create your models here.

class Post(models.Model):                                           # -5a
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)           # (auto_now_add=True)
    post_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):                                              # -5c
        return self.title

    class Meta:                                                     # -6b
        ordering = ('-post_date', )


