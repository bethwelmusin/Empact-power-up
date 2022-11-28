from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from blog.views import (
    GetAllPublishedBlogApiView,
    AddBlogApiView,
    BlogDetailApiView,
   

)

app_name='authentication'
urlpatterns = [
    path('all-published-blogs/', GetAllPublishedBlogApiView.as_view(), name='all-published-blogs'),
    path('blog-detail/', BlogDetailApiView.as_view(), name='all-published-blogs'),
    path('add-blog/<str:userId>', AddBlogApiView.as_view(), name='add-new-blog'),
    path('user-blogs/<str:userId>', AddBlogApiView.as_view(), name='user-blogs'),
    
]
