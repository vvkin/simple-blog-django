from django.urls import path
from .views import (
    BlogPostView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    AboutPageView,
)

urlpatterns = [
    path('', BlogPostView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/new/', BlogCreateView.as_view(), name='create_post'),
    path('post/<int:pk>/update/', BlogUpdateView.as_view(), name='update_post'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='delete_post'),
    path('about/', AboutPageView.as_view(), name='about')
]
