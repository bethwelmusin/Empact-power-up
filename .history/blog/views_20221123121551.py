from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.utils import timezone

from blog.serializers import *
from blog.models import *
from authentication.models import EmpactUser
from utilities.decorators import resource_checker

# Create your views here.


class GetAllPublishedBlogApiView(APIView):

    def get(self, request):
        posts = Post.published.all()
        serializer = GetPostSerializer(posts, many=True)
        return Response({
            'status': True,
            'message': 'Blog data fetched successfull',
            'status_code': status.HTTP_200_OK,
            'data': serializer.data,
        })

    def post(self, request):
        return Response({})


class AddBlogApiView(APIView):

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
    @resource_checker(Post) #This one helps us validate if the requested model data exists
    def get(self, request, userId):
        post= Posts.objects


