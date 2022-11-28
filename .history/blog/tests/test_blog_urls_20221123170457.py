from django.urls import reverse, resolve
from django.test import SimpleTestCase
from blog.views import (
    GetAllPublishedBlogApiView,
    # AddBlogApiView,
    # BlogDetailApiView,
    # CommentDetailApiView,
    # AddPostCommentApiView,
   

)

# path('all-published-blogs/', GetAllPublishedBlogApiView.as_view(), name='all-published-blogs'),
#     path('blog-detail/<int:blogId>/', BlogDetailApiView.as_view(), name='blog-detail'),
#     path('add-blog/<str:userId>/', AddBlogApiView.as_view(), name='add-new-blog'),
#     path('get-user-blogs/<str:userId>/', AddBlogApiView.as_view(), name='user-blogs'),

#     path('add-post-comment/<str:postId>/', AddPostCommentApiView.as_view(), name='comment-post'),
#     path('get-post-comments/<str:postId>/', AddPostCommentApiView.as_view(), name='get-post-comments'),

#     path('comment-detail/<str:commentId>/', CommentDetailApiView.as_view(), name='comment'),



class BlogUrlsTests(SimpleTestCase):

    def test_all_published_blogs_is_resolved(self):
        url = reverse('blog:all-published-blogs') # This the url reverse name for {all-published-blogs} url path.
        '''
        reverse comes with {func} that returns the exact view function called by the url. We shall use this to perfermo our assertion to find if its our view
        '''
        self.assertEquals(resolve(url).func.view_class, GetAllPublishedBlogApiView)
        
    def test_blog_detail_is_resolved(self):
        url = reverse('blog-detail') # This the url reverse name for {all-published-blogs} url path.
        self.assertEquals(resolve(url).func.view_class, BlogDetailApiView)
        
    def test_blog_detail_is_resolved(self):
        url = reverse('blog-detail') # This the url reverse name for {all-published-blogs} url path.
        self.assertEquals(resolve(url).func.view_class, BlogDetailApiView)