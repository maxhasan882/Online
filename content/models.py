from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from timeline.models import Album, User


class Content(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='which_content')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='whos_content')
    file = models.FileField(null=True, blank=True)

    def __str__(self):
        return str(self.file)
