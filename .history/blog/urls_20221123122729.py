from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from blog.views import (
    GetAllPublishedBlogApiView,
    LoginAPIView,
    LogoutAPIView

)

app_name='authentication'
urlpatterns = [
    path('register/', GetAllPublishedBlogApiView.as_view(), name='all-'),
    path('login/', LoginAPIView.as_view(), name='login-api'),
    path('logout/', LogoutAPIView.as_view(), name='logout-api'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh-api'),
]
