from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions

from drf_yasg.utils import swagger_auto_schema

from django.utils import timezone

from blog.serializers import *
from blog.models import *
from authentication.models import EmpactUser
from utilities.decorators import resource_checker
from utilities.error_serializer import ErrorSerializer
from rest_framework import generics

from .serializers import LikeSerializer


# Create your views here.




class GetAllPublishedBlogApiView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]

    @swagger_auto_schema(
        # request_body=GetPostSerializer,
        responses={
            '200': GetPostSerializer,
            '400': ErrorSerializer,

        },
        operation_description=' An api endpoint to get all published blogs. NOTE: When creating a blog post by default status is draft.'
    )
    def get(self, request):
        posts = Post.objects.filter(status='published').all()
        serializer = GetPostSerializer(posts, many=True)
        return Response({
            'status': True,
            'message': 'Blog data fetched successfull',
            'status_code': status.HTTP_200_OK,
            'data': serializer.data,
        })


class BlogDetailApiView(APIView):
    serializer_class = BlogPatchSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @swagger_auto_schema(
        # request_body=GetPostSerializer,
        responses={
            '200': GetPostSerializer,
            '400': ErrorSerializer,

        },
        operation_description=' An api endpoint to get blog detail. NOTE: it requires blogId parameter.'
    )
    @resource_checker(Post)
    def get(self, request, blogId):
        posts = Post.objects.filter(post_id=blogId).get()
        serializer = GetPostSerializer(posts)
        return Response({
            'status': True,
            'message': 'Blog data fetched successfull',
            'status_code': status.HTTP_200_OK,
            'data': serializer.data,
        })

    @swagger_auto_schema(
        request_body=BlogPatchSerializer,
        responses={
            '200': GetPostSerializer,
            '400': ErrorSerializer,

        },
        operation_description=' An api endpoint to patch or edit specific blog detail. NOTE: it requires blogId parameter. Provide either of the blog field to patch'
    )
    @resource_checker(Post)
    def patch(self, request, blogId):
        serializer = BlogPatchSerializer(data=request.data)

        if serializer.is_valid():
            post = Post.objects.filter(post_id=blogId).get()
            title_r = request.data.get('title')
            body_r = request.data.get('body')
            image_url_r = request.data.get('image_url')
            update_at = timezone.now().astimezone()
            if title_r is not None:
                post.title = title_r
            if body_r is not None:
                post.body = body_r
            if image_url_r is not None:
                post.image_url = image_url_r
            post.updated_at = update_at
            post.save()
            serializer = GetPostSerializer(post)
            return Response({
                'status': True,
                'message': 'Blog data updated successfull',
                'status_code': status.HTTP_200_OK,
                'data': serializer.data,
            })

        else:
            return Response({
                'status': False,
                'message': 'Operation failed',
                'status_code': status.HTTP_206_PARTIAL_CONTENT,
                'errors': serializer.errors
            })


class AddBlogApiView(APIView):
    serializer_class = NewPostSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]
    permission_classes = (permissions.IsAuthenticated,)

    @swagger_auto_schema(
        request_body=NewPostSerializer,
        responses={
            '200': GetPostSerializer,
            '400': ErrorSerializer,

        },
        operation_description='API to create a new blog post. NOTE: it requires userId parameter, tht refers to the owner of the post'
    )
    # This ensures that user Exists else it throws
    @resource_checker(EmpactUser)
    def post(self, request, userId):
        '''
        API to create a new blog post
        '''
        # Validate the request data being send
        serializer = NewPostSerializer(data=request.data)
        if serializer.is_valid():
            title = request.data.get('title')
            body = request.data.get('body')
            image_url = request.data.get('image_url')
            created_at = timezone.now().astimezone().strftime('Y-m-d')
            # Get the user creating this post if does not exist dont create post
            user = EmpactUser.objects.filter(id=userId)
            if user.exists():
                owner = user.get()
                post = Post.objects.create(
                    title=title, body=body, image_url=image_url, owner=owner, created_at=created_at, updated_at=created_at
                )
                serializer = GetPostSerializer(post)
                return Response({
                    'status': True,
                    'message': 'Blog created successfull',
                    'status_code': status.HTTP_201_CREATED,
                    'data': serializer.data,
                })
            return Response({
                'status': False,
                'message': 'Given user does not exist',
                'status_code': status.HTTP_204_NO_CONTENT,

            })

        else:
            return Response({
                'status': False,
                'message': 'Operation failed',
                'status_code': status.HTTP_206_PARTIAL_CONTENT,
                'errors': serializer.errors
            })

    @swagger_auto_schema(
        responses={
            '200': GetPostSerializer,
            '400': ErrorSerializer,

        },
        operation_description='API for Getting blog posts for a specific user. NOTE: it requires userId parameter, that refers to the owner of the post'
    )
    # This ensures that user Exists else it throws
    @resource_checker(EmpactUser)
    def get(self, request, userId):
        posts = Post.objects.filter(owner__id=userId)
        serializer = GetPostSerializer(posts, many=True)
        return Response({
            'status': True,
            'message': 'User Blogs fetched successfully',
            'status_code': status.HTTP_200_OK,
            'data': serializer.data,
        })


class AddPostCommentApiView(APIView):
    serializer_class = AddCommentSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]
    permission_classes = (permissions.IsAuthenticated,)

    @swagger_auto_schema(
        request_body=AddCommentSerializer,
        responses={
            '200': CommentSerializer,
            '400': ErrorSerializer,

        },
        operation_description='API endpoint to add a comment to a blog post. NOTE: it requires postId parameter, that refers to the specific post'
    )
    @resource_checker(Post)
    def post(self, request, postId):
        serializer = AddCommentSerializer(data=request.data)

        if serializer.is_valid():
            post = Post.objects.filter(post_id=postId).get()
            body = request.data.get('body')
            image_url = request.data.get('image_url')
            user_id = request.data.get('user_id')
            created_at = timezone.now().astimezone().strftime('Y-m-d')
            user = EmpactUser.objects.filter(id=user_id)
            if user.exists():
                comment = Comment.objects.create(
                    body=body, image_url=image_url, owner=user.get(), created_at=created_at, post=post)
                serializer = CommentSerializer(comment)
                return Response({
                    'status': True,
                    'message': 'Comment added successfully',
                    'status_code': status.HTTP_200_OK,
                    'data': serializer.data,
                })
            else:
                return Response({
                    'status': False,
                    'message': 'Given user does not exist',
                    'status_code': status.HTTP_204_NO_CONTENT,

                })

        return Response({
            'status': False,
            'message': 'Operation failed',
            'status_code': status.HTTP_206_PARTIAL_CONTENT,
            'errors': serializer.errors
        })

    @swagger_auto_schema(
        responses={
            '200': CommentSerializer,
            '400': ErrorSerializer,

        },
        operation_description='API endpoint to get comments for a specific a blog post. NOTE: it requires postId parameter, that refers to the specific post'
    )
    @resource_checker(Comment)
    def get(self, request, postId):
        comment = Comment.objects.filter(post__post_id=postId)

        serializer = CommentSerializer(comment, many=True)
        return Response({
            'status': True,
            'message': 'Post Comment fetched successfully',
            'status_code': status.HTTP_200_OK,
            'data': serializer.data,
        })


class CommentDetailApiView(APIView):
    serializer_class = CommentSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]
    permission_classes = (permissions.IsAuthenticated,)


    @swagger_auto_schema(
        responses={
            '200': CommentSerializer,
            '400': ErrorSerializer,

        },
        operation_description='API endpoint to get a specific comments. NOTE: it requires commentId parameter, that refers to the specific comment'
    )
    @resource_checker(Comment)
    def get(self, request, commentId):
        comment = Comment.objects.filter(comment_id=commentId).get()
        serializer = CommentSerializer(comment)
        return Response({
            'status': True,
            'message': 'Comment fetched successfully',
            'status_code': status.HTTP_200_OK,
            'data': serializer.data,
        })

    @swagger_auto_schema(
        request_body=CommentPatchSerializer,
        responses={
            '200': CommentSerializer,
            '400': ErrorSerializer,

        },
        operation_description='API endpoint to Patch or edit a comment. NOTE: it requires commentId parameter, that refers to the specific post\nProvide any of the required fields'
    )

    @resource_checker(Comment)
    def patch(self, request, commentId):

        serializer = CommentPatchSerializer(data=request.data)
        if serializer.is_valid():
            comment = Comment.objects.filter(comment_id=commentId).get()
            image_url = request.data.get('image_url')
            body = request.data.get('body')
            update_at = timezone.now().astimezone()
            if body is not None:
                comment.body = body
            if image_url is not None:
                comment.image_url = image_url
            comment.updated_at = update_at
            comment.save()
            serilizer = CommentSerializer(comment)
            return Response({
                'status': True,
                'message': 'Comment updated successfully',
                'status_code': status.HTTP_200_OK,
                'data': serializer.data,
            })
        return Response({
            'status': False,
            'message': 'Operation failed',
            'status_code': status.HTTP_206_PARTIAL_CONTENT,
            'errors': serializer.errors
        })





class CreateLikeView(generics.CreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = (permissions.IsAuthenticated,)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user, post=self.post)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        like = serializer.save()
        serializer = LikeSerializer(like)
        return Response({

            "status":True, 
            "message":'liked', 
            'status_code': status.HTTP_200_OK,
            "data":serializer.data
            
            })


