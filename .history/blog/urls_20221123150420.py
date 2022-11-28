from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from blog.views import (
    GetAllPublishedBlogApiView,
    AddBlogApiView,
    BlogDetailApiView,
    CommentDetailApiView,
   

)

app_name='blog'
urlpatterns = [
    path('all-published-blogs/', GetAllPublishedBlogApiView.as_view(), name='all-published-blogs'),
    path('blog-detail/<int:blogId>/', BlogDetailApiView.as_view(), name='blog-detail'),
    path('add-blog/<str:userId>/', AddBlogApiView.as_view(), name='add-new-blog'),
    path('get-user-blogs/<str:userId>/', AddBlogApiView.as_view(), name='user-blogs'),

    path('add-post-comment/<str:commentId>/', CommentDetailApiView.as_view(), name='comment'),

    path('comment-detail/<str:commentId>/', CommentDetailApiView.as_view(), name='comment'),
    path('patch-comment/<str:commentId>/', CommentDetailApiView.as_view(), name='patch-comment'),

    
]
urlpatterns = format_suffix_patterns(urlpatterns) #This one prevents 404 error when a user sends a request of a valid url but without the ending slash