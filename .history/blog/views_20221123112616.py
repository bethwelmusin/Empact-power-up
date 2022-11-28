from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .models import *

# Create your views here.

class BlogApiView(APIView)