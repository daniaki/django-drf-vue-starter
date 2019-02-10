"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="{} API".format(settings.PROJECT_NAME),
      default_version=settings.CURRENT_API_VERSION,
      description=(
          "Open access API for application developers to "
          "query '{}'.\n".format(settings.PROJECT_NAME) +
          "Current version: {}".format(settings.CURRENT_API_VERSION)
      ),
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email=settings.CONTACT_EMAIL),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

api_urlpatterns = [
    path('api/', include('api.urls'), name='api'),
    path(
       'api/swagger/',
       schema_view.with_ui('swagger', cache_timeout=0),
       name='schema-swagger-ui'
    ),
    path(
       'api/redoc/',
       schema_view.with_ui('redoc', cache_timeout=0),
       name='schema-redoc'
    ),
]


urlpatterns = [
    path('', include('index.urls'), name='index'),
]
urlpatterns += api_urlpatterns


if settings.ADMIN_ENABLED:
    urlpatterns += [path('admin/', admin.site.urls), ]
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
