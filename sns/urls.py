from django.urls import path
from .views import FriendListView
urlpatterns = [
    path('friend/', FriendListView.as_view(), name='friends')
]
