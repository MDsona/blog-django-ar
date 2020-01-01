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


class Comment(models.Model):                                        # -8a
    name = models.CharField(max_length=50, verbose_name='الاسم')    # -9c add arabic word
    email = models.EmailField(verbose_name='البريد الالكتروني')
    body = models.TextField(verbose_name='نص التعليق')
    cmnt_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_cmnt')

    def __str__(self):                                              # -8c
        return 'علق {} على {}.'.format(self.name, self.post)

    class Meta:                                                     # -8e
        ordering = ('-cmnt_date', )




