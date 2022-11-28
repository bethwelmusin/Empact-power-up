from django.shortcuts import render
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView

from utilities.decorators import resource_checker

from .serializers import *
from .models import *

# Create your views here.

class BlogApiView(APIView):

    @resource_checker(Post)
    def get(self,request):
        

