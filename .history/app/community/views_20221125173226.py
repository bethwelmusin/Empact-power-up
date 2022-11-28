from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions

from drf_yasg.utils import swagger_auto_schema

from app.utilities.error_serializer import ErrorSerializer

from .serializers import*
from .models import *

# from django.utils import timezone

# Create your views here.
class GetAllPublishedBlogApiView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]

    @swagger_auto_schema(
        responses={
            '200': CommunitySerializer,
            '400': ErrorSerializer,

        },
        operation_description=' An api endpoint to get all communities. NOTE: When creating a blog post by default status is draft.'
    )
    def get(self, request):
        community = Community.objects.filter(status='published').all()
        serializer = CommunitySerializer(community, many=True)
        return Response({
            'status': True,
            'message': 'Blog data fetched successfull',
            'status_code': status.HTTP_200_OK,
            'data': serializer.data,
        })

