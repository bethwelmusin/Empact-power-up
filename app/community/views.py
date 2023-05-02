from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema
from utilities.decorators import resource_checker

from utilities.error_serializer import ErrorSerializer

from community.serializers import *
from community.models import *

from django.utils import timezone

# Create your views here.
class GetAllCommunitiesApiView(APIView):
    # permission_classes = (permissions.IsAuthenticated,)
    @swagger_auto_schema(
        responses={
            '200': CommunitySerializer,
            '400': ErrorSerializer,

        },
        operation_description=' An api endpoint to get all communities'
    )
    def get(self, request):
        community = Community.objects.all()
        serializer = CommunitySerializer(community, many=True)
        return Response({
            'status': True,
            'message': 'Communities fetched successfull',
            'status_code': status.HTTP_200_OK,
            'data': serializer.data,
        })


class CommunityApiView(APIView):
    # permission_classes = (permissions.IsAuthenticated,)
    
    serializer_class = AddCommunitySerializer
    @swagger_auto_schema(
        request_body=AddCommunitySerializer,
        responses={
            '200': CommunitySerializer,
            '400': ErrorSerializer,

        },
        operation_description=' An api endpoint to create a new communities'
    )
    @resource_checker(EmpactUser)
    def post(self,request):
        serializer = AddCommunitySerializer(data=request.data)
        if serializer.is_valid():
            community_name = request.data.get('community_name')
            community_img = request.data.get('community_img')
            community_description = request.data.get('community_description')
            country = request.data.get('country')
            # user=EmpactUser.objects.get(id=userId)
            community= Community.objects.create(community_name=community_name,community_description=community_description,country=country,community_admin=user,community_img=community_img)
            serializer = CommunitySerializer(community)
            return Response({
                    'status': True,
                    'message': 'Community created successfull',
                    'status_code': status.HTTP_201_CREATED,
                    'data': serializer.data,
                })

        else:
            return Response({
                'status': False,
                'message': 'Operation failed',
                'status_code': status.HTTP_206_PARTIAL_CONTENT,
                'errors': serializer.errors
            })

    @swagger_auto_schema(
        responses={
            '200': CommunitySerializer,
            '400': ErrorSerializer,

        },
        operation_description=' An api endpoint to get all communities for a specific user'
    )
    @resource_checker(EmpactUser)
    def get(self,request,userId):
        community= Community.objects.filter(community_admin__id=userId)
        serializer = CommunitySerializer(community,many=True)
        return Response({
                    'status': True,
                    'message': 'Community created successfull',
                    'status_code': status.HTTP_201_CREATED,
                    'data': serializer.data,
                })

class PatchCommunityApiView(APIView):
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AddCommunitySerializer

    @swagger_auto_schema(
        request_body=PatchCommunitySerializer,
        responses={
            '200': CommunitySerializer,
            '400': ErrorSerializer,

        },
        operation_description=' An api endpoint to update a community information'
    )
    @resource_checker(Community)
    def patch(self,request,communityId):
        serializer = PatchCommunitySerializer(data=request.data)
        if serializer.is_valid():
            community_name = request.data.get('community_name')
            community_img = request.data.get('community_img')
            community_description = request.data.get('community_description')
            country = request.data.get('country')
            
            community= Community.objects.filter(community_id=communityId).get()
            if community_name is not None:
                community.community_name=community_name
            if community_img is not None:
                community.community_img=community_img
            if community_description is not None:
                community.community_description=community_description
            if country is not None:
                community.country=country
            community.save()
            serializer = CommunitySerializer(community)
            return Response({
                    'status': True,
                    'message': 'Community update successfully',
                    'status_code': status.HTTP_201_CREATED,
                    'data': serializer.data,
                })

        else:
            return Response({
                'status': False,
                'message': 'Operation failed',
                'status_code': status.HTTP_206_PARTIAL_CONTENT,
                'errors': serializer.errors
            })



class AddProjectApiView(APIView):
    serializer_class = AddProjectSerializer
  
    # permission_classes = (permissions.IsAuthenticated,)

    @swagger_auto_schema(
        request_body=AddProjectSerializer,
        responses={
            '200': ProjectSerializer,
            '400': ErrorSerializer,

        },
        operation_description='API endpoint to add a project to a community. NOTE: it requires community parameter, that refers to the specific community'
    )
    @resource_checker(Community)
    def post(self, request, communityId):
        serializer = AddProjectSerializer(data=request.data)

        if serializer.is_valid():
            community = Community.objects.filter(community_id=communityId).get()
            project_name = request.data.get('project_name')

            project_description = request.data.get('project_description')
            project_coodinator = request.data.get('project_coodinator_id')
            lifes_impacted = request.data.get('lifes_impacted')
            start_date = request.data.get('start_date')
            end_date = request.data.get('end_date')
            created_at = timezone.now().astimezone().strftime('Y-m-d')
            
            user = EmpactUser.objects.filter(id=project_coodinator)
            if user.exists():
                project = Project.objects.create(
                    community=community, project_name=project_name,
                     project_coodinator=user.get(), 
                     created_at=created_at,
                      project_description=project_description,
                      lifes_impacted=lifes_impacted,
                      start_date=start_date,
                      end_date=end_date,
                    )
                serializer = ProjectSerializer(project)
                return Response({
                    'status': True,
                    'message': 'Project added successfully',
                    'status_code': status.HTTP_200_OK,
                    'data': serializer.data,
                })
            else:
                return Response({
                    'status': False,
                    'message': 'Given user does not exist',
                    'status_code': status.HTTP_204_NO_CONTENT,

                })

        return Response({
            'status': False,
            'message': 'Operation failed',
            'status_code': status.HTTP_206_PARTIAL_CONTENT,
            'errors': serializer.errors
        })

    @swagger_auto_schema(
        responses={
            '200': ProjectSerializer,
            '400': ErrorSerializer,

        },
        operation_description='API endpoint to get projects for a specific a Community. NOTE: it requires community parameter, that refers to the specific community'
    )
    @resource_checker(Community)
    def get(self, request, communityId):
        comment = Project.objects.filter(community__community_id=communityId)

        serializer = ProjectSerializer(comment, many=True)
        return Response({
            'status': True,
            'message': 'Community project fetched successfully',
            'status_code': status.HTTP_200_OK,
            'data': serializer.data,
        })


class ProjectsDetailApiView(APIView):
    serializer_class = ProjectSerializer

    # permission_classes = (permissions.IsAuthenticated,)

    @swagger_auto_schema(
        responses={
            '200': ProjectSerializer,
            '400': ErrorSerializer,

        },
        operation_description='API endpoint to get a specific Project. NOTE: it requires project parameter, that refers to the specific project'
    )
    @resource_checker(Project)
    def get(self, request, projectId):
        project = Project.objects.filter(project_id=projectId).get()
        serializer = ProjectSerializer(project)
        return Response({
            'status': True,
            'message': 'Project fetched successfully',
            'status_code': status.HTTP_200_OK,
            'data': serializer.data,
        })

    @swagger_auto_schema(
        request_body=PatchProjectSerializer,
        responses={
            '200': ProjectSerializer,
            '400': ErrorSerializer,

        },
        operation_description='API endpoint to Patch or edit a project. NOTE: it requires projectId parameter, that refers to the specific project\nProvide any of the required fields'
    )

    @resource_checker(Project)
    def patch(self, request, projectId):

        serializer = PatchProjectSerializer(data=request.data)
        if serializer.is_valid():
            project = Project.objects.filter(project_id=projectId).get()

            project_name = request.data.get('project_name')
            project_description = request.data.get('project_description')
            project_coodinator_id = request.data.get('project_coodinator_id')
            community_id = request.data.get('community_id')
            lifes_impacted = request.data.get('lifes_impacted')
            start_date = request.data.get('start_date')
            end_date = request.data.get('end_date')
            
            update_at = timezone.now().astimezone()
            if project_name is not None:
                project.project_name = project_name
            if project_description is not None:
                project.project_description = project_description
            if project_coodinator_id is not None:
                project.project_coodinator_id = project_coodinator_id
            if community_id is not None:
                project.community_id = community_id
            if lifes_impacted is not None:
                project.lifes_impacted = lifes_impacted
            if start_date is not None:
                project.start_date = start_date
            if end_date is not None:
                project.end_date = end_date
            
            project.updated_at = update_at
            project.save()
            serializer = ProjectSerializer(project)
            return Response({
                'status': True,
                'message': 'Project updated successfully',
                'status_code': status.HTTP_200_OK,
                'data': serializer.data,
            })
        return Response({
            'status': False,
            'message': 'Operation failed',
            'status_code': status.HTTP_206_PARTIAL_CONTENT,
            'errors': serializer.errors
        })


