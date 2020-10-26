from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Post

class PostView(ListView):
    model = Post
    queryset = Post.objects.filter(draft=False).order_by("-id")

    paginate_by = 1
    template_name = "diary/post_list.html"

class PostDetailView(DetailView):
    model = Post
    slug_field = "id"