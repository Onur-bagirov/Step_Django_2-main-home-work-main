from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.posts_list, name='posts_list'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('about/', views.about, name='about'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/<slug:category_slug>/', views.category_detail, name='category_detail'),
]