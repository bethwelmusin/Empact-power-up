from .models import *
from rest_framework import serializers

# ------------------------------------- START COMMENT SERLIZERS ----------------------------------------------------
class CommunitySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Com
        fields = ['comment_id', 'body', 'owner', 'image_url', 'post']

class AddCommentSerializer(serializers.Serializer):
    body = serializers.CharField(required=False)
    image_url = serializers.CharField(required=False)
    user_id = serializers.CharField(required=False)
