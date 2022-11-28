from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from .serializers import *
from .models import *

# Create your views here.

class BlogApiView(APIView)