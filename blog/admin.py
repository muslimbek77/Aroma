from django.contrib import admin
from .models import BlogCategory, BlogPost, BlogComment
from django.utils.html import format_html

admin.site.register(BlogCategory)

admin.site.register(BlogComment)

# admin.site.register(BlogPost)
@admin.register(BlogPost)
class PlogPostAdmin(admin.ModelAdmin):
    list_display = ["title","author","img"]
    search_fields = ["title"]
    list_filter = ["author"]

    def img(self, obj):
         return format_html('<img width="100" src="{}" />'.format(obj.image.url))
