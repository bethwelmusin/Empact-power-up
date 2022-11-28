from django.urls import reverse,  resolve
from django.test import SimpleTestCase
from blog.views import GetAllPublishedBlogApiView
class ApiUrlsTests(SimpleTestCase):

    def test_allpublished-blogs_is_resolved(self):
        url = reverse('all-published-blogs') # 
        self.assertEquals(resolve(url).func.view_class, CustomerView)