from django.urls import reverse
from django.test import SimpleTestCase
class ApiUrlsTests(SimpleTestCase):

    def test_all_published_blogs_is_resolved(self):
        url = reverse('all-published-blogs') # This the url reverse name for {all-published-blogs} url path.
        print(f'RESOVE FUNC ==> {url}')
        '''
        reverse comes with {func} that 
        '''
        # self.assertEquals(resolve(url).func.view_class, GetAllPublishedBlogApiView)