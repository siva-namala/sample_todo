from django.urls import path

from . import views


app_name = 'tasks'
urlpatterns = [
    path('', views.index, name='index'),
    path('update/<str:pk>/', views.update_task, name='update_task'),
]