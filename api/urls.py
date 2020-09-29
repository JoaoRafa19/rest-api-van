from django.contrib import admin
from django.urls import path, include
from rest_api.views import *
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from . import settings
from rest_api.views import VansViewSet, MotoristaViewSet, AlunoViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'vans',VansViewSet)
router.register(r'alunos', AlunoViewSet)
router.register(r'motoristas', MotoristaViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
] + staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
