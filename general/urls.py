from django.urls import path
from .views import RatingView
urlpatterns = [
    path('post-rating/', RatingView.as_view())
]
