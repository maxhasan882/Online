from django.contrib import admin
from .models import Friend, FriendRequest, Block, Follow


admin.site.register(Friend)
admin.site.register(FriendRequest)
admin.site.register(Block)
admin.site.register(Follow)