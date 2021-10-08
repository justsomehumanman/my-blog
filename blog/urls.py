from django.urls import path
from . import views

urlpatterns = [
    path('boodoochai.pythonanywhere.com/', views.post_list, name='post_list'),
    #path('https://boodoochai.pythonanywhere.com/', views.post_list, name='post_list'),
]
