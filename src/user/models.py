from django.db import models

# Create your models here.

from django.contrib.auth.models import User                                     # -20a


class Profile(models.Model):                                                    # -20a
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')  # -20a
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):                                                          # -20e
        return f'{self.user.username} profile.'