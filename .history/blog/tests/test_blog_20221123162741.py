from django.urls import reverse,  resolve
from django.test import SimpleTestCase
from blog.views import CustomerView
class ApiUrlsTests(SimpleTestCase):

    def test_get_customers_is_resolved(self):
        url = reverse('customer')
        self.assertEquals(resolve(url).func.view_class, CustomerView)