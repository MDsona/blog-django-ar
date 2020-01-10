from django.db import models

# Create your models here.

from django.contrib.auth.models import User                                     # -20a
from django.db.models.signals import post_save                                 # -21a
from PIL import Image                                                           # -23a pillow


class Profile(models.Model):                                                    # -20a
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')  # -20a
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):                                                          # -20e
        return f'{self.user.username} profile.'

    def save(self, *args, **kwargs):                          # -23a, 23b(args, kwargs)
        super().save(*args, **kwargs)                               # , 23b

        img = Image.open(self.image.path)
        if img.width > 300 or img.height > 300:
            output_size = (300, 300)                # 300X300 px
            img.thumbnail(output_size)
            img.save(self.image.path)


def create_profile(sender, **kwarg):                                            # -21a
    if kwarg['created']:
        Profile.objects.create(user=kwarg['instance'])

post_save.connect(create_profile, sender=User)


