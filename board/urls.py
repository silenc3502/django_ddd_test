from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .board_create_view import BoardCreateView
from .board_delete_view import BoardDeleteAPIView
from .board_modify_view import BoardModifyAPIView
from .board_read_view import BoardReadAPIView
from .views import BoardViewSet

router = DefaultRouter()
router.register(r'board', BoardViewSet)  # Using 'board' instead of 'boards'


urlpatterns = [
    path('', include(router.urls)),
    path('list/', BoardViewSet.as_view({'get': 'list'}), name='board-list'),
    path('register/', BoardViewSet.as_view({'post': 'create'}), name='board-register'),
    path('read/<int:pk>/', BoardViewSet.as_view({'get': 'retrieve'}), name='board-read'),
    path('modify/<int:pk>/', BoardViewSet.as_view({'put': 'update', 'patch': 'update'}), name='board-modify'),
    path('delete/<int:pk>/', BoardViewSet.as_view({'delete': 'destroy'}), name='board-delete'),
]
