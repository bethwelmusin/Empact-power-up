
from django.contrib import admin
from django.urls import path,include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Empact API',
        default_version='v1',
        description='Api endpoints for Empact',
        contact=openapi.Contact(email="mavenwechuli@gmail.com",name=''),
    ),
    public=True,
    # permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui(
        'redoc', cache_timeout=0), name='schema-redoc'),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('authentication.urls',namespace='authentication')),
    path('api/v1/blog/', include('blog.urls',namespace='blog')),
]
