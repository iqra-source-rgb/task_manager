from django.urls import path
from . import views
from .views import TaskListCreateView, TaskDetailView

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('tasks/', views.task_list, name='task_list'),
    path('api/tasks/', TaskListCreateView.as_view(), name='api_task_list_create'),
    path('api/tasks/<int:pk>/', TaskDetailView.as_view(), name='api_task_detail'),
]
