from django.shortcuts import render
from blog.models import Category, Post
def home(request):
    featured_posts = Post.objects.filter(is_featured=True).order_by('-updated_at')[:3]
    posts = Post.objects.filter(is_featured=False, status='published').order_by('-updated_at')
    context = {
        'featured_posts': featured_posts,
        'posts': posts
    }
    return render(request, 'home.html', context)

