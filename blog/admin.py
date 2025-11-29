from django.contrib import admin
from .models import Category, Post
from django.contrib.admin import register
# Register your models here.

@register(Post)
class PostAdmin(admin.ModelAdmin):
    site_header = "Blog Administration"
    site_title = "Blog Admin Portal"
    index_title = "Welcome to the Blog Admin Area"
    list_display = ('title', 'author', 'category', 'status','is_featured')
    list_filter = ('category', 'author')
    search_fields = ('title', 'content')
    list_editable = ('status','is_featured')

@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    site_header = "Blog Administration"
    site_title = "Blog Admin Portal"
    index_title = "Welcome to the Blog Admin Area"
