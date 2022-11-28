from django.urls import reverse,  resolve
from django.test import SimpleTestCase
class ApiUrlsTests(SimpleTestCase):

    def test_all_published_blogs_is_resolved(self):
        url = reverse('all-published-blogs') # 
        self.assertEquals(resolve(url).func.view_class, GetAllPublishedBlogApiView)