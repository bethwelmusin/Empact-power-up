from blog.models import *
from rest_framework import serializers

class NewPostSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.user.username')

    class Meta:
        model = Post
        fields = ['post_id', 'title', 'body', 'image_url']

class GetPostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.first_name')
    owner_id = serializers.ReadOnlyField(source='owner.id')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['post_id','owner_id','owner', 'title', 'body', 'image_url','created_at', 'updated_at',comments]

class BlogPatchSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    body = serializers.CharField(required=False)
    image_url = serializers.CharField(required=False)