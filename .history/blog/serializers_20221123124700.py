from blog.models import *
from rest_framework import serializers

class NewPostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.user.username')

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'image_url']

class GetPostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.user.username')

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'owner', 'image_url','created_at']

class BlogPatchSerializer(serializers.Serializer):
    branch_name = serializers.CharField(required=True)
    restaurant_image = serializers.CharField(required=True)