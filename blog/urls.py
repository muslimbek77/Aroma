from django.urls import path
from .views import BlogPostView,PostDetailView

urlpatterns = [
    path('',BlogPostView.as_view(),name='blog-page'),
    path('<int:pk>/',PostDetailView.as_view(),name='blog-detail-view')
    
]