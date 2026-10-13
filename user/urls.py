from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('add/', views.add_view, name='add'),
    path('update/<int:pk>/', views.update_view, name='update'),
    path('delete/<int:pk>/', views.delete_view, name='delete'),
]