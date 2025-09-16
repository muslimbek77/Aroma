from django.urls import path
from .views import home_page, blog_page

urlpatterns = [
    path('', home_page, name='home-page'),
    path('blog', blog_page, name='blog-page'),
]

