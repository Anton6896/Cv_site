from django.db import models
from accounts.models import CustomUser
from PIL import Image
from django.utils import timezone


def customer_image_file_path(instance, filename):
    import os
    import uuid
    """Generate file path for new image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join('upload/message_pic/', filename)


class MessageManager(models.Manager):
    """
    is an manager :
    Message.objects.all()
    Message.objects.crete(author=user, title=title etc...)
    etc...

    """

    # override the all method (shew only un read messages)
    # def all(self, *args, **kwargs):
    #     return super(MessageManager, self).filter(is_read=False)
    pass


class Mesage(models.Model):
    objects = MessageManager()  # activate manager
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    # slug -> for link instead of pk (still dont know if i want to use it) ?
    # slug = models.SlugField(unique=True)
    image = models.ImageField(default='default.jpg',
                              upload_to=customer_image_file_path)
    created_at = models.DateTimeField(default=timezone.now)
    # update update time for message
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    content = models.TextField()
    priority = models.IntegerField(default=0)
    is_read = models.BooleanField(default=False)

    STATUS_CHOICES = (
        ('done', 'done'),
        ('working_on', 'working_on'),
        ('on_hold', 'on_hold'),
    )
    TAG_CHOICES = (
        ('message', 'message'),
        ('issue', 'issue'),
    )
    tag = models.CharField(choices=TAG_CHOICES,
                           max_length=15, default='message')
    status = models.CharField(choices=STATUS_CHOICES,
                              max_length=15, default='working_on')

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
        return self.title + "__ by: " + self.author.username

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("message:detail", kwargs={"pk": self.pk})

    def is_pass_week(self):
        # this is util function for requirement to
        # send notification if pass a week in issue message
        return timezone.now() == self.created_at + timezone.timedelta(days=7)

    def is_issue(self):
        return self.tag == 'issue'

    class Meta:
        ordering = ["-timestamp", "-created_at"]

# class Comment(models.Model):
#     author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     message = models.ForeignKey(Mesage, on_delete=models.CASCADE)
#     # comment = models.ForeignKey(self, on_delete=models.CASCADE)
#
#     created_at = models.DateTimeField(default=timezone.now)
#     content = models.TextField()
#
#     def __str__(self):
#         return "comment by : " + self.author.username + " , for: " + self.message.title