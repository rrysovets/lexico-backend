from django.urls import include, path

from rest_framework.routers import DefaultRouter
from core.apps.modules.views import ModuleViewSet

router = DefaultRouter()
router.register(r'modules', ModuleViewSet, basename='module')

urlpatterns = [
    path('', include(router.urls)),
]



