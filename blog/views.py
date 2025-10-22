from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DetailView
from .models import BlogPost
from hitcount.views import HitCountMixin


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

class PostDetailView(HitCountMixin, DetailView):
        model = BlogPost
        template_name = 'single-blog.html'
        count_hit = True

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)

            hit_count = self.get_object().hit_count
            hit_count_response = self.hit_count(self.request, hit_count)

            context['hitcount'] = hit_count_response
            return context