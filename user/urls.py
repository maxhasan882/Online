from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from .views import UserCreateView, PassWordReset, ResetPasswordConfirm

urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserCreateView.as_view(), name='user-create'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('reset/', PassWordReset.as_view(), name='password-reset'),
    path('confirm-password/', ResetPasswordConfirm.as_view(), name='confirm-password-reset')
]
