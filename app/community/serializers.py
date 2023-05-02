from authentication.serializers import EmpactUserWithoutCommentSerializer
from community.models import *
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    project_coodinator = serializers.ReadOnlyField(source='project_coodinator.first_name')
    class Meta:
        model = Project
        fields = ['project_id', 'project_name','project_description', 'project_coodinator', 'community','project_status','lifes_impacted', 'start_date','end_date','created_at']

class AddProjectSerializer(serializers.Serializer):
    project_name = serializers.CharField(required=True)
    project_description = serializers.CharField(required=True)
    project_coodinator_id = serializers.CharField(required=True)
    lifes_impacted = serializers.CharField(required=True)
    start_date = serializers.DateTimeField(required=True)
    end_date = serializers.DateTimeField(required=True)

class PatchProjectSerializer(serializers.Serializer):
    project_name = serializers.CharField(required=False)
    project_description = serializers.CharField(required=False)
    project_coodinator_id = serializers.CharField(required=False)
    community_id = serializers.CharField(required=False)
    lifes_impacted = serializers.CharField(required=False)
    start_date = serializers.DateTimeField(required=False)
    end_date = serializers.DateTimeField(required=False)




# ------------------------------------- START Community SERLIZERS ----------------------------------------------------
class CommunitySerializer(serializers.ModelSerializer):
    projects = serializers.SerializerMethodField()
    members = EmpactUserWithoutCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Community
        fields = ['community_id', 'community_name','community_img','community_admin', 'community_description','verified', 'country','membersCount', 'members','projectsCount','projects','created_at']

    def get_projects(self,obj):
        proj = Project.objects.filter(community__community_id=obj.community_id).all()
        serializers = ProjectSerializer(proj,many=True)
        return serializers.data

class AddCommunitySerializer(serializers.Serializer):
    community_name = serializers.CharField(required=True)
    community_img = serializers.ImageField(required=True)
    community_description = serializers.CharField(required=True)
    country = serializers.CharField(required=True)
    community_admin = serializers.CharField(required=True)

class PatchCommunitySerializer(serializers.Serializer):
    community_name = serializers.CharField(required=False)
    community_img = serializers.ImageField(required=True)
    community_description = serializers.CharField(required=False)
    country = serializers.CharField(required=False)



