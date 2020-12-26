from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from accounts.models import CustomUser


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # message = models.ForeignKey(Mesage, on_delete=models.CASCADE, default='')
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    def __str__(self):
        return f'comment for: " {self.message.title} "  , < by {self.user.username} > '
