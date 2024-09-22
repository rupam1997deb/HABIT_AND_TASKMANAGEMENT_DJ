from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('habits/', views.habit_list, name='habit_list'),
    path('habits/add/', views.add_habit, name='add_daily_habit'),
    path('habits/update/<int:habit_id>', views.update_habit, name = 'update_habit'),
    path('habits/delete/<int:habit_id>', views.delete_habit, name = 'delete_habit'),
    path('download_habits/', views.download_habits_csv, name='download_habits'),

    path('tasks/', views.task_list, name='task_list'),
    path('tasks/add/', views.add_task, name='add_task'),
    path('tasks/update/<int:task_id>', views.update_task, name='update_task'),
    path('tasks/delete/<int:task_id>', views.delete_task, name='delete_task'),
    path('download-tasks/', views.download_tasks, name='download_tasks'),
]