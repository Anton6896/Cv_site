from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import secrets
import os


# extend the user profile model
class Profile(models.Model):
    # on user create have an signal at signal.py to crete profile for this user  ******
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        try:
            img = Image.open(self.image.path)
            output_size = (300, 300)

            if img.height > 300 or img.width > 300:
                img.thumbnail(output_size)
                img.save(self.image.path)
        except IOError:
            print(f'where is the file for img working ?')


class GuestProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.