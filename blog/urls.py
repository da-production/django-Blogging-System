from django.urls import path
from . import views
urlpatterns = [
    path('test_api/', views.test_api, name='test_api'),
    path('category/<int:category_id>/', views.category_posts, name='category_posts'),
    path('posts/<str:slug>/', views.post_detail, name='post_detail')
]