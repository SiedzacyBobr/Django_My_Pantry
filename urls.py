from django.urls import path
from .import views


urlpatterns = [
    path('', views.main, name='main'),
    path('adding/', views.adding, name='adding'),
    path('my_pantry/', views.my_pantry, name='my_pantry'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('go/', views.go_shopping, name='go'),
    path('with/', views.with_shopping, name='with'),
    path('to_kitchen/<int:pk>/', views.to_kitchen, name='to_kitchen'),
    path('action_shopping/<int:pk>/', views.action_shopping, name='action_shopping'),
    path('category/', views.my_category, name="category"),
    path('add_cate/', views.add_category, name='add_cate'),
    path('delete_cate/<int:pk>/', views.delete_cate, name='delete_cate'),
    path('update_cate/<int:pk>/', views.update_cate, name='update_cate'),


    
]