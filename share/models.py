from django.db import models
from django.db.models import CASCADE

from timeline.models import Post
from user.models import User


class Share(models.Model):
    post = models.ForeignKey(Post, on_delete=CASCADE, related_query_name='share_post')
    user = models.ForeignKey(User, on_delete=CASCADE, related_query_name='share_user')
    caption = models.CharField(max_length=100)

    Public = 'Public'
    Private = 'Private'
    Friends = 'Friends'

    visibility_choice_list = [
        (Public, 'Public'),
        (Private, 'Private'),
        (Friends, 'Friends'),
    ]

    visibility_mode = models.CharField(max_length=10, choices=visibility_choice_list, default=Public)

    def __str__(self):
        return self.caption
