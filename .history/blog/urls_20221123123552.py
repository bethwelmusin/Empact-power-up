from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from blog.views import (
    GetAllPublishedBlogApiView,
    AddBlogApiView,
   

)

app_name='authentication'
urlpatterns = [
    path('all-published-blogs/', GetAllPublishedBlogApiView.as_view(), name='all-published-blogs'),
    path('login/', AddBlogApiView.as_view(), name='login-api'),
    
]
