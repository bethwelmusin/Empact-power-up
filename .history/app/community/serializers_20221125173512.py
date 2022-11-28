from app.authentication.serializers import EmpactUserWithoutCommentSerializer
from app.community.models import *
from rest_framework import serializers

# ------------------------------------- START COMMENT SERLIZERS ----------------------------------------------------
class CommunitySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    members = EmpactUserWithoutCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Community
        fields = ['community_id', 'community_name', 'community_description', 'country', 'members',,'created_at']

class AddCommunitySerializer(serializers.Serializer):
    community_name = serializers.CharField(required=True)
    community_description = serializers.CharField(required=True)
    country = serializers.CharField(required=True)
    community_admin = serializers.CharField(required=True)

