from django.db import models
from django.contrib.auth import get_user_model as user_model
User = user_model()


class Friend(models.Model):
    who = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend_who')
    whom = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend_whom')
    date = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('who', 'whom')

    def __str__(self):
        return self.who.name + " to " + self.whom.name


class FriendRequest(models.Model):
    who = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Friend_request_who')
    whom = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Friend_request_whom')
    date = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('who', 'whom')

    def __str__(self):
        return self.who.name + " to " + self.whom.name


class Block(models.Model):
    who = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Block_who')
    whom = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Block_whom')
    date = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('who', 'whom')

    def __str__(self):
        return self.who.name + " to " + self.whom.name


class Follow(models.Model):
    who = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Follow_who')
    whom = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Follow_whom')
    date = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('who', 'whom')

    def __str__(self):
        return self.who.name + " to " + self.whom.name
