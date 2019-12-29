from django.contrib import admin

from .models import Post, Comment            # -5b

# Register your models here.

admin.site.register(Post)           # -5b
admin.site.register(Comment)           # -8b
