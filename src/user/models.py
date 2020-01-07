from django.db import models

# Create your models here.

from django.contrib.auth.models import User                                     # -20a
from django.db.models.signals import post_save                                 # -21a


class Profile(models.Model):                                                    # -20a
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')  # -20a
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):                                                          # -20e
        return f'{self.user.username} profile.'


def create_profile(sender, **kwarg):                                            # -21a
    if kwarg['created']:
        Profile.objects.create(user=kwarg['instance'])

post_save.connect(create_profile, sender=User)


