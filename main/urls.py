from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('', views.index, name='home'),
    path('post/<slug:post_slug>/', views.post_detail, name='post_detail'),
    path('create/', views.create_post, name='create_post'),
]
