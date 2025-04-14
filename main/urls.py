from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='home'),
    path('post/<slug:post_slug>/', views.post_detail, name='post_detail'),
]
