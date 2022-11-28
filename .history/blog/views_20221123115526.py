from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


from blog.serializers import *
from blog.models import *
from authentication.models import EmpactUser

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
    def post(self,request):
        return Response({})

class AddBlogApiView(APIView):

    # @resource_checker(Post)
    def post(self, request,userId):
        serializer = NewPostSerializer(data=request.data)
        if serializer.is_valid():
            title = request.data.get('title')
            body = request.data.get('body')
            image_url = request.data.get('image_url')
            user=EmpactUser.objects.filter(id=userId)
            
            post = Post(
               title=title, body=body,image_url=image_url,
            )

        else:
            return Response({
                'status': False,
                'message': 'Operation failed',
                'status_code': status.HTTP_206_PARTIAL_CONTENT,
                'errors': serializer.errors
            })

        
    