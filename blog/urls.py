from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),

    path('', views.post_list, name='blog_list'),


    path('<int:pk>/', views.post_detail, name='post_detail'),
    
    path('<int:pk>/delete/', views.post_delete, name='post_delete'), 


    path('comment/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
]


