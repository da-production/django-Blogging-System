from django.contrib import admin
from .models import Category, Post
from django.contrib.admin import register
# Register your models here.

@register(Post)
class PostAdmin(admin.ModelAdmin):
    site_header = "Blog Administration"
    site_title = "Blog Admin Portal"
    index_title = "Welcome to the Blog Admin Area"


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    site_header = "Blog Administration"
    site_title = "Blog Admin Portal"
    index_title = "Welcome to the Blog Admin Area"
