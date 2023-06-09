from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.utils import timezone
from authentication.models import EmpactUser
from blog.models import Post

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
    def setUp(self):
        self.user = User.objects.create_user(
            username='admin', password='admin')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        empact_user= EmpactUser.objects.create(
            user=self.user,first_name='mavin',last_name='wechuli',
            mobile_number='+254799143482',email='mavenwechuli@gmai.com',
        )
        created_at = timezone.now().astimezone().strftime('Y-m-d')
        self.userUuId = empact_user.id

        add_post_url = reverse('blog:add-new-blog', args=[self.userUuId])

        data = {
            "owner": self.userUuId,
            "body": "Johnson published MOrisee post",
            "image_url": "https://images.unsplash.com/photo-1580121521203-ab94824d9382?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8ZGphbmdvfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=800&q=60",
            "title": 'EmpactUser test',
            "created_at": created_at,
            "updated_at":created_at
        }
        self.client.post(
            add_post_url, data, format='json')
        
        post = Post.objects.create(
            owner= empact_user,
            body= "Johnson published MOrisee postj",
            image_url= "https=//images.unsplash.com/photo-1580121521203-ab94824d9382?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8ZGphbmdvfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=800&q=60",
            title= 'EmpactUser tester',
            created_at= created_at,
            updated_at=created_at
        )
        self.postId=post.post_id
        

    def test_get_blog_detail_autheticated(self):
        post_detail_url = reverse('blog:blog-detail', args=[self.postId])
        response = self.client.get(post_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['data']['title'], 'EmpactUser tester')
        self.assertEqual(response.data['data']['body'], 'Johnson published MOrisee postj')

    def test_patch_blog_detail_autheticated(self):
        post_detail_url = reverse('blog:blog-detail', args=[self.postId])
        data={
            "title":"Being empactful"
        }
        response = self.client.patch(post_detail_url,data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['data']['title'], 'Being empactful')
        self.assertEqual(response.data['data']['body'], 'Johnson published MOrisee postj')

    def test_get_blog_detail_unautheticated(self):
        self.client.force_authenticate(user=None, token=None)
        post_detail_url = reverse('blog:blog-detail', args=[self.postId])
        response = self.client.get(post_detail_url)
        self.assertEqual(response.status_code, 401)
        
    def test_patch_blog_detail_unautheticated(self):
        self.client.force_authenticate(user=None, token=None)
        post_detail_url = reverse('blog:blog-detail', args=[self.postId])
        data={
            "title":"Being empactful"
        }
        response = self.client.patch(post_detail_url,data, format='json')
        self.assertEqual(response.status_code, 401)
        

class CommentDetailAPIViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='admin', password='admin')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        empact_user= EmpactUser.objects.create(
            user=self.user,first_name='mavin',last_name='wechuli',
            mobile_number='+254799143482',email='mavenwechuli@gmai.com',
        )
        created_at = timezone.now().astimezone().strftime('Y-m-d')
        self.userUuId = empact_user.id

        post = Post.objects.create(
            owner= empact_user,
            body= "Johnson published MOrisee postj",
            image_url= "https=//images.unsplash.com/photo-1580121521203-ab94824d9382?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8ZGphbmdvfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=800&q=60",
            title= 'EmpactUser tester',
            created_at= created_at,
            updated_at=created_at
        )
        self.postId=post.post_id

        data = {
            "owner": self.userUuId,
            "body": "Johnson published MOrisee post comment",
            "image_url": "https://images.unsplash.com/photo-1580121521203-ab94824d9382?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8ZGphbmdvfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=800&q=60",
            "post": self.postId,
            "created_at": created_at,
            "updated_at":created_at
        }
        comment_url = reverse('blog:comment-post', args=[self.postId])
        self.client.post(
            comment_url, data, format='json')

    def test_get_post_comment_autheticated(self):
        comment_url = reverse('blog:get-post-comments', args=[self.postId])
        response = self.client.get(comment_url)
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.data['data']['title'], 'EmpactUser tester')
        # self.assertEqual(response.data['data']['body'], 'Johnson published MOrisee post comment')

    def test_patch_comment_detail_autheticated(self):
        comment_detail_url = reverse('blog:comment', args=[1])
        data={
            "body":"Being empactful"
        }
        response = self.client.patch(comment_detail_url,data, format='json')
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.data['data']['body'], 'Being empactful')

    def test_get_comment_detail_autheticated(self):
        comment_detail_url = reverse('blog:comment', args=[1])
        
        response = self.client.get(comment_detail_url, format='json')
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.data['data']['body'], 'Being empactful')
