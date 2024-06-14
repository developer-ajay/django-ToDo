
from django.shortcuts import render

from todo.models import task


def home(request):
    tasks = task.objects.filter(is_completed= False)
    context = {
        'tasks' : tasks
    }
    return render(request , 'home.html',context)