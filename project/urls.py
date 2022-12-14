
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# from django.conf.urls import url
# from rest_framework_swagger.views import get_swagger_view

# schema_view = get_swagger_view(title='FINTECH API DOCUMENTATION')

schema_view = get_schema_view(
   openapi.Info(
      title="FINTECH API DOCUMENTATION",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.myapp.com/policies/terms/",
      contact=openapi.Contact(email="henryanorue1@gmail.com"),
      license=openapi.License(name="FINTECH License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api_docs/', schema_view),
    path('', include('speedapp.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), 
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
