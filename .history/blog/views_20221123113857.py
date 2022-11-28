from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from utilities.decorators import resource_checker

from blog.serializers import *
from blog.models import *

# Create your views here.

class BlogApiView(APIView):

    @resource_checker(Post)
    def get(self,request):
        posts = Post.published.all()
        serializer = GetPostSerializer(posts, many=True)
        return Response({
                                'status':True,
                                'message':'B successfull',
                                'status_code':status.HTTP_200_OK,
                                'data':serializer.data,
                            })

