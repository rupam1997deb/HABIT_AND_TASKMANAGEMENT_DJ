from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . models import DailyHabitLog, DailyTask
from django.utils import timezone
import csv

def home(request):
    return render(request, 'home.html')

def habit_list(request):
    habits = DailyHabitLog.objects.all().order_by('date')
    return render (request, 'habit_list.html', {'habits': habits})

def add_habit(request):
    if request.method == 'POST':
        DailyHabitLog.objects.create(
            date=request.POST.get('date') or timezone.now().date(),
            wakeup_time=request.POST.get('wakeup_time'),
            gratitude_written=request.POST.get('gratitude_written'),
            workout_done=request.POST.get('workout_done'),
            book_reading_done=request.POST.get('book_reading_done'),
            python_problems_solved=request.POST.get('python_problems_solved'),
            python_advanced=request.POST.get('python_advanced'),
            asleep_by_midnight=request.POST.get('asleep_by_midnight')
        )
        return redirect('habit_list')  # Redirect to habit list page after submission
    return render(request, 'add_habit.html')


def update_habit(request, habit_id):
    habit = get_object_or_404(DailyHabitLog, id = habit_id)
    if request.method == 'POST':
        habit.date=request.POST.get('date')
        habit.wakeup_time=request.POST.get('wakeup_time')
        habit.gratitude_written=request.POST.get('gratitude_written')
        habit.workout_done=request.POST.get('workout_done')
        habit.book_reading_done=request.POST.get('book_reading_done')
        habit.python_problems_solved=request.POST.get('python_problems_solved')
        habit.python_advanced=request.POST.get('python_advanced')
        habit.asleep_by_midnight=request.POST.get('asleep_by_midnight')
        habit.save()
        return redirect('habit_list')
    return render(request, 'update_habit.html', {'habit': habit})


def delete_habit(request, habit_id):
    habit = get_object_or_404(DailyHabitLog, id = habit_id)
    if request.method == 'POST':
        habit.delete()
        return redirect('habit_list')
    return render(request, 'delete_habit.html', {'habit': habit})

def download_habits_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="habit_logs.csv"'
    writer = csv.writer(response)
    writer.writerow(['Date', 'Woke Up by 6:30 AM', 'Gratitude Written', 'Completed Workout',
                     'Book Reading Completed', 'Solved 5 Python Problems','Learning Advanced Python Topics',
                     'Asleep by 12:00 AM' ])

    habits = DailyHabitLog.objects.all()  
    for habit in habits:
        writer.writerow([
            habit.date,
            habit.wakeup_time,
            habit.gratitude_written,
            habit.workout_done,
            habit.book_reading_done,
            habit.python_problems_solved,
            habit.python_advanced,
            habit.asleep_by_midnight,   
        ])
    return response


def add_task(request):
    if request.method == 'POST':
        
        date = request.POST.get('date') or timezone.now().date()
        task_name = request.POST.get('task_name')
        status = request.POST.get('status')
        category = request.POST.get('category')
        roadblocks = request.POST.get('roadblocks').strip()  
        
        DailyTask.objects.create(
            date=date,
            task_name=task_name,
            status=status,
            category=category,
            roadblocks=roadblocks,
        )
        return redirect('task_list')
    
    return render(request, 'add_task.html')

def task_list(request):
    tasks = DailyTask.objects.all().order_by('date')
    return render(request, 'task_list.html', {'tasks': tasks})


def update_task(request, task_id):
    task = get_object_or_404(DailyTask, id = task_id)
    if request.method == 'POST':
        task.date=request.POST.get('date') or timezone.now().date()
        task.task_name = request.POST.get('task_name')
        task.status = request.POST.get('status')
        task.category = request.POST.get('category')
        task.roadblocks = request.POST.get('roadblocks')
        
        task.save()
        return redirect('task_list')
    return render(request, 'update_task.html', {'task': task})


def delete_task(request, task_id):
    task = get_object_or_404(DailyTask, id = task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'delete_task.html', {'task': task})

def download_tasks(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="tasks.csv"'

    writer = csv.writer(response)
    writer.writerow(['Date', 'Task Name', 'Status', 'Category', 'Task Description'])

    # Fetch tasks from the database
    tasks = DailyTask.objects.all().values_list('date', 'task_name', 'status', 'category', 'roadblocks')

    for task in tasks:
        writer.writerow(task)

    return response


