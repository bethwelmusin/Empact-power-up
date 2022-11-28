from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions


from django.utils import timezone

from blog.serializers import *
from blog.models import *
from authentication.models import EmpactUser
from utilities.decorators import resource_checker
from utilities.permissions import IsOwnerOrReadOnly


# Create your views here.


class GetAllPublishedBlogApiView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    def get(self, request):
        posts = Post.objects.filter(status='published').all()
        serializer = GetPostSerializer(posts, many=True)
        return Response({
            'status': True,
            'message': 'Blog data fetched successfull',
            'status_code': status.HTTP_200_OK,
            'data': serializer.data,
        })

    def post(self, request):
        return Response({})

class BlogDetailApiView(APIView):
    serializer_class = BlogPatchSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          ]
    @resource_checker(Post)
    def get(self, request,blogId):
        posts = Post.objects.filter(post_id=blogId)
        serializer = GetPostSerializer(posts, many=True)
        return Response({
            'status': True,
            'message': 'Blog data fetched successfull',
            'status_code': status.HTTP_200_OK,
            'data': serializer.data,
        })
    @resource_checker(Post)
    def patch(self, request, blogId):
        serializer =BlogPatchSerializer(data=request.data)
        
        if serializer.is_valid():
            post = Post.objects.filter(post_id=blogId).get()
            title_r = request.data.get('title')
            body_r = request.data.get('body')
            image_url_r = request.data.get('image_url') 
            update_at=timezone.now().astimezone()
            if title_r is not None:
                post.title=title_r
            if body_r is not None:
                post.body=body_r
            if image_url_r is not None:
                post.image_url = image_url_r
            post.updated_at=update_at
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

        return Response({})


class AddBlogApiView(APIView):
    serializer_class = NewPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    # @resource_checker(Post)
    def post(self, request, userId):
        '''API to create a new blog post
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

    ''''Getting posts for a specific user'''
    def get(self, request, userId):
        posts= Post.objects.filter(owner__id=userId)
        serializer = GetPostSerializer(posts, many=True)
        return Response({
            'status': True,
            'message': 'User Blogs fetched successfully',
            'status_code': status.HTTP_200_OK,
            'data': serializer.data,
        })



class CommentDetailApiView(APIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    @resource_checker(Comment)                     
    def get(self,request,commentId):
        comment= Comment.objects.filter(comment_id=commentId)
        serializer = CommentSerializer(comment)
        return Response({
            'status': True,
            'message': 'Comment fetched successfully',
            'status_code': status.HTTP_200_OK,
            'data': serializer.data,
        })
    @resource_checker(Comment)  
    def patch(self,request,commentId):
        
        serializer = CommentPatchSerializer(data=request.data)
        if serializer.is_valid():
            comment= Comment.objects.filter(comment_id=commentId).get()
            image_url= request.data.get('image_url') 
            body = request.data.get('body') 
            update_at=timezone.now().astimezone()
            if title_r is not None:
                post.title=title_r
            return Response({
                'status': True,
                'message': 'Comment fetched successfully',
                'status_code': status.HTTP_200_OK,
                'data': serializer.data,
            })
        return Response({
            'status': False,
            'message': 'Operation failed',
            'status_code': status.HTTP_206_PARTIAL_CONTENT,
            'errors': serializer.errors
        })
       
