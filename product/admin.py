from django.contrib import admin
from .models import Category, Product, Wishlist, Review

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Wishlist)
admin.site.register(Review)