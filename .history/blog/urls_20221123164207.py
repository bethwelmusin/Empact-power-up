from django.urls import path
from blog import views as api_views

app_name='blog'
urlpatterns = [
    path('all-published-blogs/', api_views.GetAllPublishedBlogApiView.as_view(), name='allpublished_blogs'),
    path('blog-detail/<int:blogId>/', api_views.BlogDetailApiView.as_view(), name='blog-detail'),
    path('add-blog/<str:userId>/', api_views.AddBlogApiView.as_view(), name='add-new-blog'),
    path('get-user-blogs/<str:userId>/', api_views.AddBlogApiView.as_view(), name='user-blogs'),

    path('add-post-comment/<str:postId>/', api_views.AddPostCommentApiView.as_view(), name='comment-post'),
    path('get-post-comments/<str:postId>/', api_views.AddPostCommentApiView.as_view(), name='get-post-comments'),

    path('comment-detail/<str:commentId>/', api_views.CommentDetailApiView.as_view(), name='comment'),
    # path('patch-comment/<str:commentId>/', CommentDetailApiView.as_view(), name='patch-comment'),

    
]
# NOTE: I COMMENTED THIS OUT INFAVOR OF SWAGGER, THAT WILL DUPLICATE EACH API WITH {format}
# urlpatterns = format_suffix_patterns(urlpatterns) #This one prevents 404 error when a user sends a request of a valid url but without the ending slash