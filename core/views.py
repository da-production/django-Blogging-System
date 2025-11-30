from django.shortcuts import render, get_object_or_404
from blog.models import Category, Post
def home(request):
    featured_posts = Post.objects.filter(is_featured=True).order_by('-updated_at')[:3]
    posts = Post.objects.filter(is_featured=False, status='published').order_by('-updated_at')
    context = {
        'featured_posts': featured_posts,
        'posts': posts
    }
    return render(request, 'home.html', context)

def category_posts(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category_id=category_id).order_by('-updated_at')
    context = {
        'posts': posts,
        'category': category
    }
    return render(request, 'category_posts.html', context)