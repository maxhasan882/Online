from django.urls import path
from .views import ShareView
urlpatterns = [
    path('share-post/', ShareView.as_view())
]
