from django.shortcuts import render
from django.views.generic.list import ListView
from .models import BlogPost


class BlogPostView(ListView):
    model = BlogPost
    template_name = "blog.html"
    context_object_name = "blogs"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        most_view = BlogPost.objects.order_by('-created_at')[:4]
        context['popular_posts'] = most_view

        return context