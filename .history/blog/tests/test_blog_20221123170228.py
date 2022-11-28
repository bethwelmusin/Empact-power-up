from django.urls import reverse
from django.test import SimpleTestCase



class BlogUrlsTests(SimpleTestCase):

    def test_all_published_blogs_is_resolved(self):
        url = reverse('blog:all-published-blogs') # This the url reverse name for {all-published-blogs} url path.
        print(f'RESOVE FUNC ==> {url}')
        '''
        reverse comes with {func} that returns the exact view function called by the url. We shall use this to perfermo our assertion to find if its our view
        '''
        self.assertEquals(resolve(url).func.view_class, GetAllPublishedBlogApiView)