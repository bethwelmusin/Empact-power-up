from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.utils import timezone
from authentication.models import EmpactUser
from blog.models import Post
import json

class PostAPIViewTests(APITestCase):
    post_url = reverse('blog:all-published-blogs')

    def setUp(self):
        self.user = User.objects.create_user(
            username='admin', password='admin')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_all_published_blogs_authenticated(self):
        response = self.client.get(self.post_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_published_blogs_unauthenticated(self):
        self.client.force_authenticate(user=None, token=None)
        response = self.client.get(self.post_url)
        self.assertEquals(response.status_code, 401)


class PostDetailAPIViewTests(APITestCase):
    post_detail_url = reverse('blog:blog-detail', args=[1])
    add_post_url = reverse('blog:add-new-blog', args=[1])

    def setUp(self):
        self.user = User.objects.create_user(
            username='admin', password='admin')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        

    def test_get_blog_detail_autheticated(self):
        response = self.client.get(self.post_detail_url)
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.data['title'], 'Blog')
        # self.assertEqual(response.data['owner'], 'self.user')

    def test_add_blog_autheticated(self):
        created_at = timezone.now().astimezone().strftime('Y-m-d')
        user = User.objects.create_user(
            username='admintest', password='admin')

        empact_user= EmpactUser.objects.create(user=user,first_name='mavin',last_name='wechuli',
        mobile_number='+254799143482',email='mavenwechuli@gmai.com',
        )
        post = Post.objects.create(
            owner= empact_user,
            "body"= "Johnson published MOrisee post",
            "image_url"= "https=//images.unsplash.com/photo-1580121521203-ab94824d9382?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8ZGphbmdvfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=800&q=60",
            "title"= 'EmpactUser test',
            "created_at"= created_at,
            "updated_at"=created_at
        )
        data = {
            "owner": json.dumps(empact_user),
            "body": "Johnson published MOrisee post",
            "image_url": "https://images.unsplash.com/photo-1580121521203-ab94824d9382?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8ZGphbmdvfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=800&q=60",
            "title": 'EmpactUser test',
            "created_at": created_at,
            "updated_at":created_at
        }
        self.client.post(
            self.add_post_url, data, format='json')
        
        response = self.client.get(self.post_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Blog')
