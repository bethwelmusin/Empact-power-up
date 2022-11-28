from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    RegisterAPIView,
    LoginAPIView,
    LogoutAPIView

)

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register-api'),
    path('login/', LoginAPIView.as_view(), name='login-api'),
    path('logout/', LogoutAPIView.as_view(), name='logout-api'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh-api'),
]
