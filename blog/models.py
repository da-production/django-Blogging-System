from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=100, help_text="A unique identifier for the category, used in URLs.", editable=False, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:  # Only populate slug if empty
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.slug} - {'Active' if self.is_active else 'Inactive'}"
    
STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    ('archived', 'Archived'),
    ('deleted', 'Deleted'),
    ('under_review', 'Under Review'),
    ('private', 'Private'),
)
class Post(models.Model):
    author = models.OneToOneField(User,max_length=100, null=True, blank=True, on_delete=models.SET_NULL, related_name='posts')
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200, help_text="A unique identifier for the post, used in URLs.", editable=False)
    content = models.TextField(null=True, blank=True)
    excerpt = models.TextField(max_length=160,null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    featured_image = models.ImageField(upload_to='updloads/posts/images/%Y/%m/%d', null=True, blank=True)
    

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-published_at']

    def save(self, *args, **kwargs):
        if not self.slug:  # Only populate slug if empty
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {'Published' if self.status else 'Draft'}"