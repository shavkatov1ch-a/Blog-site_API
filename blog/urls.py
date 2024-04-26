from django.urls import path
from .views import PostAPIView, TagAPIView, PostDetailAPIView


urlpatterns = [
    path('post/', PostAPIView.as_view(), name='post'),
    path('post/<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),
    path('tag/', TagAPIView.as_view(), name='tag')
]