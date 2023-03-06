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
]