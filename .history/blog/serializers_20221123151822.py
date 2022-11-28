from blog.models import *
from rest_framework import serializers

# ------------------------------------- 
class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ['comment_id', 'body', 'owner', 'image_url', 'post']

class AddCommentSerializer(serializers.Serializer):
    body = serializers.CharField(required=False)
    image_url = serializers.CharField(required=False)
    user_id = serializers.CharField(required=False)

class CommentPatchSerializer(serializers.Serializer):
    body = serializers.CharField(required=False)
    image_url = serializers.CharField(required=False)


class NewPostSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.user.username')

    class Meta:
        model = Post
        fields = ['post_id', 'title', 'body', 'image_url']

class GetPostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.first_name')
    owner_id = serializers.ReadOnlyField(source='owner.id')
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['post_id','owner_id','owner', 'title', 'body', 'image_url','created_at', 'updated_at','comments']

class BlogPatchSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    body = serializers.CharField(required=False)
    image_url = serializers.CharField(required=False)
