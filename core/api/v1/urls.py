from django.urls import include, path

from rest_framework.routers import DefaultRouter
from core.apps.modules.views import ModuleViewSet,GenerateThemeView, ThemeResultView


router = DefaultRouter()
router.register(r'modules', ModuleViewSet, basename='module')

urlpatterns = [
    path('', include(router.urls)),
    path('generate-theme', GenerateThemeView.as_view(), name='generate-theme'),
    path('generate-theme-result/<str:task_id>', ThemeResultView.as_view(), name='theme-result')
]



