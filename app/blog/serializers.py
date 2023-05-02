from blog.models import *
from rest_framework import serializers



# like button




class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'post', 'is_deleted', 'created_at']
    def validate(self, attrs):
        user = attrs.get("user")
        post = attrs.get("post")
        if user and post:
            return attrs
        raise serializers.ValidationError(
            {
                "user": "User id is required",
                "post": "Post id is required"})
    def create(self, validated_data):
        user = validated_data["user"]
        post = validated_data["post"]

        like_qs = Like.objects.filter(user=user, post=post, is_deleted=False)
        if not like_qs.exists():
            like_obj = Like.objects.create(user=user, post=post)
            return like_obj
        # like_obj = like_qs.delete()
        like_qs.update(is_deleted=True)
        like_obj = Like.objects.get(user=user, post=post)
        return like_obj



# ------------------------------------- START COMMENT SERLIZERS ----------------------------------------------------
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
# ------------------------------------- END COMMENT SERILIZERS ----------------------------------------------------

#-------------------------------------- START BLOG POST SERLIZERS -------------------------------------------------

class NewPostSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.user.username')

    class Meta:
        model = Post
        fields = ['post_id', 'title', 'body', 'image_url']

class GetPostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.first_name')
    owner_id = serializers.ReadOnlyField(source='owner.id')
    comments = CommentSerializer(many=True, read_only=True)
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['post_id','owner_id','owner', 'title', 'body', 'image_url', 'likes', 'created_at', 'updated_at','comments']

    def get_likes(self,obj):
        count = Like.objects.filter(post=obj.post_id, is_deleted=False).count()
        return count

class BlogPatchSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    body = serializers.CharField(required=False)
    image_url = serializers.CharField(required=False)

# ------------------------------------------ END BLOG POST SERLIZERS ----------------------------------------------------