from django.urls import path
from community.views import (
    GetAllCommunitiesApiView,
    CommunityApiView,
    PatchCommunityApiView,
    AddProjectApiView,
    ProjectsDetailApiView,


)

app_name = 'community'
urlpatterns = [
    path('all-communities/', GetAllCommunitiesApiView.as_view(),
         name='all-communities'),
    path('community/<str:userId>/', CommunityApiView.as_view(), name='community'),
    path('patch-community/<str:communityId>/', PatchCommunityApiView.as_view(), name='patch-community'),

    path('community-project/<str:communityId>/', AddProjectApiView.as_view(), name='community-projects'),
    path('project-detail/<str:projectId>/', ProjectsDetailApiView.as_view(), name='project-detail'),

]
# NOTE: I COMMENTED THIS OUT INFAVOR OF SWAGGER, THAT WILL DUPLICATE EACH API WITH {format}
# urlpatterns = format_suffix_patterns(urlpatterns) #This one prevents 404 error when a user sends a request of a valid url but without the ending slash
