from django.urls import path
from .import views




urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/create/', views.task_create, name='task_create'),
]

# after defining the app routes
# we take the url patterns and register to the project

