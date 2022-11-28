from django.urls import reverse, resolve
from django.test import SimpleTestCase
# from rest_framework.test import APITestCase, APIClient
from blog.views import (
    GetAllPublishedBlogApiView,
    CommentDetailApiView,
    AddPostCommentApiView,
    AddBlogApiView,
    BlogDetailApiView,
)

class AllBlogUrlsTests(SimpleTestCase):

    def test_all_published_blogs_is_resolved(self):
        # This the url reverse name for {all-published-blogs} url path.
        url = reverse('blog:all-published-blogs')
        '''
        reverse comes with {func} that returns the exact view function called by the url. We shall use this to perfermo our assertion to find if its our view
        '''
        self.assertEquals(resolve(url).func.view_class,
                          GetAllPublishedBlogApiView)

    def test_blog_detail_is_resolved(self):
        # This the url reverse name for {all-published-blogs} url path.Requires and id add it in args
        url = reverse('blog:blog-detail', args=[1])
        self.assertEquals(resolve(url).func.view_class, BlogDetailApiView)

    def test_add_new_blog_is_resolved(self):
        # This the url reverse name for {all-published-blogs} url path.Requires and id add it in args

        add_blog_url = reverse('blog:add-new-blog', args=[1])
        # This the url reverse name for {all-published-blogs} url path.Requires and id add it in args

        get_user_blog_url = reverse('blog:add-new-blog', args=[1])

        self.assertEquals(
            resolve(add_blog_url).func.view_class, AddBlogApiView)
        self.assertEquals(
            resolve(get_user_blog_url).func.view_class, AddBlogApiView)

    def test_add_post_comment_is_resolved(self):
        # This the url reverse name for {all-published-blogs} url path.Requires and id add it in args

        comment_post_url = reverse('blog:comment-post', args=[1])
        # This the url reverse name for {all-published-blogs} url path.Requires and id add it in args

        get_post_comment_url = reverse('blog:get-post-comments', args=[1])

        self.assertEquals(
            resolve(comment_post_url).func.view_class, AddPostCommentApiView)
        self.assertEquals(
            resolve(get_post_comment_url).func.view_class, AddPostCommentApiView)

    def test_comment_detail_is_resolved(self):
        # This the url reverse name for {all-published-blogs} url path.Requires and id add it in args

        url = reverse('blog:comment', args=[1])
        self.assertEquals(resolve(url).func.view_class, CommentDetailApiView)
