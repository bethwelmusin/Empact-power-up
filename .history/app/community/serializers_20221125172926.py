from app.authentication.serializers import EmpactUserWithoutCommentSerializer
from app.community.models import *
from rest_framework import serializers

# ------------------------------------- START COMMENT SERLIZERS ----------------------------------------------------
class CommunitySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    members = EmpactUserWithoutCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Community
        fields = ['community_id', 'community_name', 'community_description', 'country', 'members','created_at']

class AddCommunitySerializer(serializers.Serializer):
    community_name = serializers.CharField(required=False)
    community_description = serializers.CharField(required=False)
    country = serializers.CharField(required=False)
    country = serializers.CharField(required=False)
  

# community_id = models.UUIDField(
#         primary_key=True, default=uuid.uuid4, editable=False, unique=True)
#     community_name = models.CharField(max_length=100, )
#     community_description = models.CharField(max_length=400, )  
#     country = models.CharField(max_length =50, default='Kenya')
#     members = models.ForeignKey(EmpactUser, related_name='community', on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     deleted_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=True)
