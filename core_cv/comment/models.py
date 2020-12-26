from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from accounts.models import CustomUser
from message.models import Mesage


class CommentManager(models.manager):
    def filter_by_instance(self, instance):
        # instance.__class__  -> return the instance by class for more generic use
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.pk
        return super(CommentManager, self).filter(content_type=content_type, object_id=obj_id)


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.ForeignKey(Mesage, on_delete=models.CASCADE, null=True, blank=True)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    objects = CommentManager()

    def __str__(self):
        if self.message:
            return f'comment for: " {self.message.title} "  , < by {self.user.username} > '
        else:
            return f'comment: {self.pk}  , < by {self.user.username} > for comment {self.parent.pk}'
