from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_blog, name = 'all_blog'),
    path('<int:post_id>/', views.detail, name = 'detail'),
]
