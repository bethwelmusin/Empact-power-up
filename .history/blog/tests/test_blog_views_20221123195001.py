from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.utils import timezone
from django.core import serializers
from authentication.models import EmpactUser


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

    def setUp(self):
        self.user = User.objects.create_user(
            username='admin', password='admin')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        

    def test_get_blog_detail_autheticated(self):
        
        
        response = self.client.get(self.post_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Blog')
        self.assertEqual(response.data['owner'], 'self.user')

    def test_add_blog_detail_autheticated(self):
        created_at = timezone.now().astimezone().strftime('Y-m-d')
        user = User.objects.create_user(
            username='admin', password='admin')
        
        id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.OneToOneField(
        User, null=False, on_delete=models.CASCADE)
    first_name = models.CharField(db_column='firstname', max_length=50,null=False, blank=False)
    last_name = models.CharField(db_column='lastname', max_length=50,null=False, blank=False)
    mobile_number = models.CharField(max_length=13)
    email = models.CharField(max_length=100, null=False, blank=False)
    country = models.CharField(max_length=100, null=False, blank=False, default='Kenya')
    profile_pic_url = models.CharField(max_length=100, null=True, blank=True)
    member_type = models.CharField(
        max_length=100, choices=MEMBER_TYPE, default='Community')
    user_type = models.CharField(
        max_length=100, choices=USER_ROLES, default='EmpactUser')
    updated_on = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
        empact_user= EmpactUser.objects.create()
        data = {
            "title": "Blog",
            "body": "Johnson published MOrisee",
            "image_url": "https://images.unsplash.com/photo-1580121521203-ab94824d9382?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8ZGphbmdvfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=800&q=60",
            "owner": user,
            "created_at": created_at,
            "updated_at":created_at
        }
        self.client.post(
            self.post_detail_url, data, format='json')
        
        response = self.client.get(self.post_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Blog')
        self.assertEqual(response.data['owner'], 'self.user')
