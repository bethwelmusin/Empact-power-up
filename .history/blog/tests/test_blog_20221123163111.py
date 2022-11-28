from django.urls import reverse,  resolve
from django.test import SimpleTestCase
from blog.views import GetAllPublishedBlogApiView
class ApiUrlsTests(SimpleTestCase):

    def test_all_published_blogs_is_resolved(self):
        url = reverse('all-published-blogs') # This the url reverse name for {all-published-blogs} url path.
        '''
        reverse comes with {func} f
        '''
        self.assertEquals(resolve(url).func.view_class, GetAllPublishedBlogApiView)