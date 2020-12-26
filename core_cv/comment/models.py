from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from accounts.models import CustomUser


class CommentManager(models.Manager):
    def filter_by_instance(self, instance):
        # instance.__class__  -> return the instance by class for more generic use
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.pk
        return super(CommentManager, self).filter(content_type=content_type, object_id=obj_id)


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)

    # generic foreign key
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    objects = CommentManager()

    def __str__(self):
        return f'comment: {self.object_id}'
