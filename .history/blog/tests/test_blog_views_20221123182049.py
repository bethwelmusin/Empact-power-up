from django.urls import reverse, resolve
from django.test import SimpleTestCase
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from blog.views import (
    # GetAllPublishedBlogApiView,
    # CommentDetailApiView,
    # AddPostCommentApiView,
    # AddBlogApiView,
    # BlogDetailApiView,
)

class CustomerAPIViewTests(APITestCase):
    customers_url = reverse("customer")

    def setUp(self):
        self.user = User.objects.create_user(
            username='admin', password='admin')
        self.token = Token.objects.create(user=self.user)
        #self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_customers_authenticated(self):
        response = self.client.get(self.customers_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_customers_un_authenticated(self):
        self.client.force_authenticate(user=None, token=None)
        response = self.client.get(self.customers_url)
        self.assertEquals(response.status_code, 401)

    def test_post_customer_authenticated(self):
        data = {
            "title": "Mr",
            "name": "Peter",
            "last_name": "Parkerz",
            "gender": "M",
            "status": "published"
        }
        response = self.client.post(self.customers_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 8)
