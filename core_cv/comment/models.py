from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from accounts.models import CustomUser


class CommentManager(models.Manager):
    def filter_by_instance(self, instance):
        # instance.__class__  -> return the instance by class for more generic use
        content_type = ContentType.objects.get_for_model(instance.__class__)  # return Message
        obj_id = instance.pk  # return message.pk
        return super(CommentManager, self).filter(content_type=content_type, object_id=obj_id)


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    objects = CommentManager()
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    """
    generic foreign key
    will crete object with data that referenced to some table (db) with some key 
    without checking if its exist ! 
    
    example:
    just saving the content fot message with pk 2 , 
    its dissent marrow if message with this key is exist al all 
    the comment with this data will be exist ! 
    """
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_pk = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_pk')

    def __str__(self):
        return f'comment for "{self.content_type}" with id {self.object_pk} , by <{self.user.username}>'
