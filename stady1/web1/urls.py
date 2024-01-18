from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('addpage/', views.addpage),
    path('contact/', views.contact),
    path('login/', views.login),
    path('post/<int:post_id>/', views.show_post, name='post')

]
