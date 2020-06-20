from django.urls import path
from .views import (
    BlogPostView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
)

urlpatterns = [
    path('', BlogPostView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/new/', BlogCreateView.as_view(), name='create_post'),
    path('post/<int:pk>/update/', BlogUpdateView.as_view(), name='update_post'),
]
