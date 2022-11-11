from django.views.generic import ListView, DetailView
from .models import Post


# template_name 설정 안하면 post_list.html 로 자동 설정
class PostList(ListView):
    model = Post
    ordering = "-pk"
    # template_name = 'blog.html'


class PostDetail(DetailView):
    model = Post