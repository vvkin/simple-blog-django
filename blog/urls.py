from django.urls import path
from .views import (
    BlogPostView, 
    BlogDetailView,
    BlogCreateView,
)

urlpatterns = [
    path('', BlogPostView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post'),
    path('post/new/', BlogCreateView.as_view(), name='create_post')
]
