from django.urls import path

from .views import index,posts_list

urlpatterns = [
    path('', index, name='index'),
    path('posts_list/', posts_list, name='posts_list'),
]