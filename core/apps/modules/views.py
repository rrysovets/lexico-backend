from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets, views, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from celery.result import AsyncResult

from core.apps.modules.permissions import IsOwnerOrReadOnly
from .models import Module
from .serializers import ModuleSerializer
from .tasks import get_generated_module

class ModuleViewSet(viewsets.ModelViewSet):
    serializer_class = ModuleSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_public']
    search_fields = ['title']
    ordering_fields = ['created_at', 'updated_at', 'title']
    ordering = ['-created_at']

    # @method_decorator(cache_page(60 * 5))  # 5 минут
    # def list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)

    # @method_decorator(cache_page(60 * 10))  # 10 минут
    # def retrieve(self, request, *args, **kwargs):
    #     return super().retrieve(request, *args, **kwargs)

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:  # Для администраторов показываем все модули
            return Module.objects.all()
        # Для обычных пользователей показываем их собственные модули и публичные
        return Module.objects.filter(Q(author=user) | Q(is_public=True))

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def toggle_like(self, request, pk=None):
        obj = self.get_object()
        user = request.user
        
        
        if user in obj.likes.all():
            obj.likes.remove(user)
            liked = False
        else:
            obj.likes.add(user)
            liked = True
            
        return Response({
            "rating": obj.rating,
            "liked": liked
        })

class GenerateThemeView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        theme = request.query_params.get('theme')
        count_of_words = request.query_params.get('count_of_words')
        if not theme:
            return Response({"error": "Missing 'theme' parameter"}, status=400)
        task = get_generated_module.delay(theme,count_of_words)
        return Response({"task_id": task.id}, status=202)

class ThemeResultView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, task_id, *args, **kwargs):
        result = AsyncResult(task_id)
        if result.state == 'PENDING':
            return Response({"status": "pending"})
        elif result.state == 'STARTED':
            return Response({"status": "started"})
        elif result.state == 'FAILURE':
            return Response({"status": "failure", "error": str(result.result)})
        elif result.state == 'SUCCESS':
            return Response({"status": "success", "data": result.result})
        return Response({"status": result.state})