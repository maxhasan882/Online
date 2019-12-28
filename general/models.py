from django.db import models

from timeline.models import Post
from user.models import User


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    rate = models.FloatField()

    def __str__(self):
        return str(self.rate)
