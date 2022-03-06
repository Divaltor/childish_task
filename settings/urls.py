"""settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken

schema_view = get_schema_view(
    openapi.Info(
        title="Car documentation",
        default_version='v1',
        description="Lorem ipsum",
        terms_of_service="It's free, dude ;)",
        contact=openapi.Contact(email="contact@divaltor.ru"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    authentication_classes=[TokenAuthentication]
)


api_patterns = [
    path('', include('car_management.urls')),
    path('', include('base.urls'))
]

auth_patterns = [
    path('auth/', ObtainAuthToken.as_view())
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_patterns + auth_patterns)),
    path('docs/swagger', schema_view.with_ui('swagger', cache_timeout=0))
]
