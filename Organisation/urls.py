from django.urls import path
from . import views
urlpatterns = [
    path('doleances/', views.doleances, name='doleances'),
]