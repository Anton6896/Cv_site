from django.db import models
from accounts.models import CustomUser
import os
import uuid
from PIL import Image
from django.utils import timezone


def customer_image_file_path(instance, filename):
    """Generate file path for new image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('upload/message_pic/', filename)


class Mesage(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = models.ImageField(default='default.jpg',
                              upload_to=customer_image_file_path)
    created_at = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    STATUS_CHOICES = (
        ('done', 'done'),
        ('working_on', 'working_on'),
        ('on_hold', 'on_hold'),
    )
    status = models.CharField(choices=STATUS_CHOICES,
                              max_length=15, default='working_on')

    priority = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        """change img size"""
        super(Mesage, self).save(*args, **kwargs)

        try:
            img = Image.open(self.image.path)
            output_size = (300, 300)

            if img.height > 300 or img.width > 300:
                img.thumbnail(output_size)
                img.save(self.image.path)
        except IOError:
            print(f'where is the file for img working ?')

    def __str__(self):
        return " _("+self.title + " : by - " + self.user.username + ")_ "
