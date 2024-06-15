
from django.shortcuts import render
from django.utils import timezone
from todo.models import Task


def home(request):
    today = timezone.now().date()
    tasks = Task.objects.filter(is_completed= False , created_at__date=today)
    completed_tasks = Task.objects.filter(is_completed= True , created_at__date=today)
    context = {
        'tasks' : tasks,
        'completed_tasks' : completed_tasks
    }
    return render(request , 'home.html',context)