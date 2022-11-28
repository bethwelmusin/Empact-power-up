from django.urls import path
from app.community.views import (
    GetAllCommunitiesApiView,

   

)

app_name='community'
urlpatterns = [
    path('all-communities/', GetAllCommunitiesApiView.as_view(), name='all-communities'),
   
]
# NOTE: I COMMENTED THIS OUT INFAVOR OF SWAGGER, THAT WILL DUPLICATE EACH API WITH {format}
# urlpatterns = format_suffix_patterns(urlpatterns) #This one prevents 404 error when a user sends a request of a valid url but without the ending slash