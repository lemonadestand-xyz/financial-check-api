"""plaid_rest_celery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers
from submissions.views import SubmissionViewSet

detail_router = routers.SimpleRouter()
detail_router.register(r'submissions', SubmissionViewSet, 'submissions')

schema_view = get_schema_view(
    openapi.Info(
        title="Plaid integration with REST and celery",
        default_version='v1',
        description="Few crazy out there who are willing to change the world will change it",
        terms_of_service="",
        contact=openapi.Contact(email="mjrulesamrat@gmail.com"),
        license=openapi.License(name=""),
    ),
    public=False,
    permission_classes=(permissions.IsAdminUser,),
)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/',
                       include((detail_router.urls, 'api-v2'), )
                       ),
                  path('api/v1/', include('djoser.urls')),
                  path('api/v1/', include('djoser.urls')),
                  path('api/v1/auth/', include('djoser.urls.authtoken')),

                  path('api/v1/plaid/', include('plaidapp.urls'), name='plaid'),

                  path('api/v1/docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
                  path('', include('users.urls')),
                  path('', include('submissions.urls')),
                  path('accounts/', include('django.contrib.auth.urls')),
              ] + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
)
