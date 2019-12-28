from django.db import models
from user.models import User
from django.contrib.contenttypes.fields import GenericRelation


class Album(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Post(models.Model):
    post_text = models.TextField(max_length=200)
    date_time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='who_posted')
    post_content = GenericRelation('content.Content', related_query_name='post_content_rev')

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
        return self.post_text[:10]
