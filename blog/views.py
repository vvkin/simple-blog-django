from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)
from .models import Post


class BlogPostView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'one_post.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'
